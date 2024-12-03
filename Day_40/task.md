# Task: Find and Notify Cheapest Flights to Destinations

## Objective:
The task is to retrieve data from a Google Sheet containing destinations, find the cheapest flights to these destinations from a specified origin city (Delhi, IATA code: "DEL"), and send notifications for flights that are below a certain price threshold. The system uses various modules to interact with flight data, manage destination codes, and notify users via SMS for cheap flight deals.

## Requirements:
1. **Python 3.x**: Ensure Python 3.x is installed.
2. **External Libraries**:
   - `requests`: For making HTTP requests to external APIs.
   - `time`: For managing delays between API requests to avoid rate limits.
   - `data_manager`: A custom module for managing destination data from a Google Sheet.
   - `flight_search`: A custom module for searching flight data.
   - `notification_manager`: A custom module for sending SMS notifications.

   You can install necessary libraries using:
   ```bash
   pip install requests
   ```

3. **Google Sheets API**: The system uses the Google Sheets API to store and retrieve destination data. Ensure that the appropriate API keys are set up and configured.

4. **Twilio API**: Twilio is used for sending SMS notifications. You will need an account with Twilio and the following:
   - Twilio API credentials (Account SID and Auth Token)
   - A Twilio phone number to send SMS from

## Modules and Functionality:

### 1. **DataManager**:
   The `DataManager` class is responsible for handling the destination data stored in Google Sheets. It allows you to:
   - Retrieve destination data (`get_destination_data()`).
   - Update destination data (`update_destination_codes()`).

### 2. **FlightSearch**:
   The `FlightSearch` class is used to search for flights based on the given origin city and destination. It allows you to:
   - Retrieve IATA codes for cities (`get_destination_code()`).
   - Find the cheapest flight to a destination in the next month (`find_cheapest_flight_in_next_month()`).

### 3. **NotificationManager**:
   The `NotificationManager` class is responsible for sending SMS notifications. It allows you to:
   - Send SMS with a message body (`send_sms()`).

### 4. **FlightData**:
   The `find_cheapest_flight` function is used to find the cheapest flight from the flight data returned by `FlightSearch`. It helps extract the relevant details about the flight, such as:
   - Price
   - Origin and destination airports
   - Dates of the flight

## Process:

### 1. **Retrieve Data from Google Sheets**:
   - The `DataManager` object is initialized, and the `get_destination_data()` method is called to retrieve the destination data stored in the Google Sheet.
   - Each destination row should contain:
     - `city`: Name of the city.
     - `iataCode`: IATA code for the city (this will be populated if empty).
     - `lowestPrice`: The lowest price previously recorded for a flight to this destination.

### 2. **Update IATA Codes**:
   - The script checks if any destination row has an empty `iataCode`.
   - If an IATA code is missing, the script fetches the IATA code for the city using the `get_destination_code()` method from the `FlightSearch` class. This code is then added to the corresponding row.
   - There is a `time.sleep(2)` delay between each API request to avoid exceeding the rate limit of the flight API.

### 3. **Find Flights**:
   - The script loops through each destination in the `sheet_data` and calls `find_cheapest_flight_in_next_month()` from the `FlightSearch` class.
   - This function fetches the flight data (e.g., prices, flight dates, etc.) for the next month for each destination from the origin city (`DEL`).

### 4. **Find Cheapest Flight**:
   - Once the flight data is retrieved, the `find_cheapest_flight()` function is called to identify the cheapest flight from the list of available options.
   - The function returns an object that contains:
     - `price`: The price of the flight.
     - `origin_airport`: The airport from which the flight departs.
     - `destination_airport`: The airport where the flight arrives.
     - `out_date`: The departure date of the flight.
     - `return_date`: The return date of the flight.
   - If no flight is found or the price is "N/A", the destination is skipped.

### 5. **Send Notifications**:
   - If the cheapest flight found has a price lower than the `lowestPrice` recorded in the Google Sheet, the script sends an SMS notification using the `NotificationManager`'s `send_sms()` method.
   - The message contains:
     - The new flight price.
     - The origin and destination airports.
     - The flight's departure and return dates.

   The message is formatted as follows:
   ```
   Low price alert! Only £<price> to fly from <origin_airport> to <destination_airport>, from <out_date> to <return_date>.
   ```

### 6. **Update Google Sheet**:
   - If a lower price is found, the `lowestPrice` value in the Google Sheet for the corresponding destination is updated to the new price.
   - The updated data is saved back to the Google Sheet using the `update_destination_codes()` method from the `DataManager`.

### 7. **Rate Limiting**:
   - There are `time.sleep(2)` delays added between each API request to manage rate limiting and ensure the script runs smoothly without hitting API request limits.

## Steps to Set Up:

1. **Obtain API Keys**:
   - **Google Sheets API**: Set up access to the Google Sheets API and create a service account. Download the credentials and set them up as environment variables or in a JSON file.
   - **Twilio API**: Create a Twilio account, obtain your `Account SID`, `Auth Token`, and a phone number for sending SMS.

2. **Set Environment Variables**:
   - Set up the following environment variables:
     - `SHEETY_URL`: Your Sheety URL to access the Google Sheet.
     - `API_KEY`: Your Nutritionix or flight data API key.
     - `APP_ID`: Your Nutritionix application ID.
     - `AUTH_TOKEN`: Your Twilio Auth Token.

3. **Run the Script**:
   - Execute the script in a Python environment. Ensure that all required environment variables are set and that you have access to the relevant APIs.

## Expected Output:
- A Google Sheet will be populated with the lowest price data for each destination.
- SMS notifications will be sent when cheaper flights are found to any of the destinations.

## Troubleshooting:
- **API Rate Limits**: Ensure that you are adhering to the rate limits set by the external APIs (flight search, Google Sheets, etc.). If necessary, increase the sleep time between requests.
- **Missing Data**: Ensure that the Google Sheet contains valid city names and `lowestPrice` values before running the script.
- **Twilio SMS**: Ensure that your Twilio credentials are correct and that you have a verified Twilio phone number for sending SMS messages.

## Notes:
- The script assumes the Google Sheet contains a list of cities with empty IATA codes that need to be populated.
- The flight search and notification processes are performed for each destination sequentially, which may take some time depending on the number of destinations.

```