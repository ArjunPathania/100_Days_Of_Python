from dotenv import load_dotenv,find_dotenv
import requests
import os
from datetime import datetime

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

load_dotenv(find_dotenv())

class FlightSearch:
    def __init__(self):
        self._api_key=os.environ["API_KEY"]
        self._api_secret = os.environ["API_SECRET"]
        self._token=self._get_new_token()

    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        response.raise_for_status()
        # print(f"Your token is {response.json()['access_token']}")
        # print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']

    def get_destination_code(self, city_name):
        print(f"Using this token to get destination {self._token}")
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(
            url=IATA_ENDPOINT,
            headers=headers,
            params=query
        )
        print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {
            "Authorization": f"Bearer {self._token}",
            "Content-Type": "application/json"
        }

        query = {
            "currencyCode": "GBP",
            "originDestinations": [
                {
                    "id": "1",
                    "originLocationCode": origin_city_code,
                    "destinationLocationCode": destination_city_code,
                    "departureDateTimeRange": {
                        "date": from_time.strftime("%Y-%m-%d")
                    }
                }
            ],
            "travelers": [
                {
                    "id": "1",
                    "travelerType": "ADULT"
                }
            ],
            "sources": [
                "GDS"
            ],
            "searchCriteria": {
                "maxPrice": None,  # Replace None with max_price if you need to limit price
                "maxFlightOffers": 10,
                "flightFilters": {
                    "cabinRestrictions": [
                        {
                            "cabin": "ECONOMY",
                            "coverage": "MOST_SEGMENTS",
                            "originDestinationIds": ["1"]
                        }
                    ]
                }
            }
        }

        response = requests.post(
            url=FLIGHT_ENDPOINT,
            headers=headers,
            json=query
        )

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            print(response.json())
            return None

        return response.json()


