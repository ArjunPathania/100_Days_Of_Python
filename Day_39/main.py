import time
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import find_cheapest_flight  # Import FlightData and find_cheapest_flight

# Initialize objects
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()  # No need to pass token, it's handled in the class
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "DEL"

# Update destination data with IATA codes
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(2)

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

# Find and notify for the cheapest flight to each destination
for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights_data = flight_search.find_cheapest_flight_in_next_month(
        ORIGIN_CITY_IATA,
        destination["iataCode"]
    )

    if flights_data:
        # Pass the retrieved flights data to find the cheapest flight
        cheapest_flight = find_cheapest_flight(flights_data)

        if cheapest_flight and cheapest_flight.price != "N/A":
            print(f"{destination['city']}: £{cheapest_flight.price}")
            time.sleep(2)

            # If a lower price is found, send an SMS notification
            if cheapest_flight.price < destination["lowestPrice"]:
                print(f"Lower price flight found to {destination['city']}!")
                notification_manager.send_sms(
                    message_body=f"Low price alert! Only £{cheapest_flight.price} to fly from "
                                 f"{cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                                 f"from {cheapest_flight.out_date} to {cheapest_flight.return_date}."
                )
