class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date


def find_cheapest_flight(data):
    if data is None:
        print("No flight data received.")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    # If 'data' key is missing or empty, handle that case
    if 'data' not in data or not data['data']:
        print("No flight data found in response:", data)
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    # Assuming the first flight is the cheapest initially
    first_flight = data['data'][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0] if len(first_flight["itineraries"]) > 1 else "N/A"

    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)

    # Loop through the data to find the actual cheapest flight
    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0] if len(flight["itineraries"]) > 1 else "N/A"
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)
            print(f"Lowest price to {destination} is £{lowest_price}")

    return cheapest_flight

