import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"


def find_cheapest_flight(data):
    """
    Finds the cheapest flight from the given flight data.
    """
    if not data['data']:
        return None

    cheapest_flight = min(data['data'], key=lambda x: float(x['price']['grandTotal']))
    price = float(cheapest_flight["price"]["grandTotal"])
    origin = cheapest_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = cheapest_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    out_date = cheapest_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = "N/A"
    if len(cheapest_flight["itineraries"]) > 1:
        return_date = cheapest_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

    return {
        'price': price,
        'origin': origin,
        'destination': destination,
        'out_date': out_date,
        'return_date': return_date
    }


class FlightSearch:

    def __init__(self):
        """
        Initializes the FlightSearch instance and retrieves an API token.
        """
        self._api_key = os.environ["API_KEY"]
        self._api_secret = os.environ["API_SECRET"]
        self._token = self._get_new_token()

    def _get_new_token(self):
        """
        Retrieves a new authentication token from Amadeus API.
        """
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        # print(f"Your token is {response.json()['access_token']}")
        return response.json()['access_token']

    def get_destination_code(self, city_name):
        """
        Retrieves the IATA code for the specified city from Amadeus API.
        """
        print(f"Using token to get destination {self._token}")
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
        try:
            code = response.json()["data"][0]['iataCode']
        except (IndexError, KeyError):
            print(f"Error finding IATA code for {city_name}.")
            return "Not Found"
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):
        """
        Searches for flights between two cities for a given date range.
        """
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "INR",
            "max": "5",  # Limit the number of results to avoid rate limits
        }

        response = requests.get(
            url=FLIGHT_ENDPOINT,
            headers=headers,
            params=query,
        )

        if response.status_code != 200:
            print(f"check_flights() error: {response.status_code}")
            return None

        return response.json()

    def find_cheapest_flight_in_next_month(self, origin_city_code, destination_city_code):
        today = datetime.today()
        next_month = today + timedelta(days=30)  # Approximate next month
        flights_data = self.check_flights(
            origin_city_code,
            destination_city_code,
            from_time=today,
            to_time=next_month
        )

        if flights_data and flights_data.get("data"):
            return find_cheapest_flight({"data": flights_data["data"]})
        else:
            return None  # Return None explicitly when no flights are found



