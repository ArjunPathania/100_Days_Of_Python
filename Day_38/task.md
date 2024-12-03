# Task: Log Exercise Data to Sheety using Nutritionix API

## Objective:
Create a Python script to track exercise activities using the Nutritionix API. The script logs the exercise data to a Google Sheet using the Sheety API. The process involves sending the exercise details to Nutritionix for calorie and duration estimation, and then logging this data into a Google Sheet for later review.

## Requirements:
1. **Python 3.x**: Ensure Python 3.x is installed on your system.
2. **External Libraries**:
   - `requests`: For making HTTP requests to APIs.
   - `os`: To interact with environment variables.
   - `datetime`: For handling date and time formatting.
   - You can install the required libraries using:
     ```bash
     pip install requests
     ```

3. **API Keys**:
   - **Nutritionix API Key**: This key is needed to access the Nutritionix API for exercise data. Obtain it from [Nutritionix](https://developer.nutritionix.com/).
   - **Sheety API Key**: This key is used to authenticate requests to the Sheety API, which is required to log data to your Google Sheets. Obtain it by creating an account on [Sheety](https://sheety.co/).
   - **Environment Variables**:
     - Set up the following environment variables:
       - `API_KEY`: Your Nutritionix API Key.
       - `APP_ID`: Your Nutritionix Application ID.
       - `SHEETY_URL`: Your Sheety URL path for the workout log.
       - `AUTH_TOKEN`: Your authentication token for Sheety.

## Process:

### 1. **Get User Input for Exercise**:
   - The user is prompted to input the exercise they performed.
   - This input is captured and sent to the Nutritionix API to estimate the calories burned and the duration of the exercise.

### 2. **Send Exercise Data to Nutritionix API**:
   - The user's exercise query, along with profile data (such as gender, weight, height, and age), is sent to the Nutritionix API using the `POST` method.
   - Nutritionix returns data including the exercise name, duration, and calories burned, which are then extracted for further use.

### 3. **Parse and Extract Exercise Data**:
   - The response from the Nutritionix API includes a list of exercises with details like the exercise name, duration in minutes, and calories burned.
   - The relevant details (exercise name, duration, and calories) are extracted and formatted into a list of tuples for logging purposes.

### 4. **Log Data to Sheety**:
   - The exercise data is formatted to match the required structure for Sheety, which includes the date, time, exercise name, duration, and calories.
   - Each workout entry is logged individually to the Sheety endpoint using the `POST` method, with the required headers for authentication.

### 5. **Handle Responses**:
   - The script prints the response status of each API request to help debug and verify that the data is being sent and received correctly.
   - If the POST request to Sheety is successful, the workout data will be logged in the corresponding Google Sheet.

## Expected Output:
- A Google Sheet (via Sheety) will be populated with data about the exercises you've done. Each entry will have:
  - **Date**: The current date when the exercise was logged.
  - **Time**: The time the exercise was performed.
  - **Exercise**: The name of the exercise performed.
  - **Duration**: The number of minutes spent on the exercise.
  - **Calories**: The estimated number of calories burned during the exercise.

## Steps:
1. **Obtain the necessary API keys** for Nutritionix and Sheety.
2. **Set the environment variables** (`API_KEY`, `APP_ID`, `SHEETY_URL`, `AUTH_TOKEN`).
3. **Run the script** to log your exercise data to Sheety.
4. **Check the Sheety Google Sheet** for logged workout data.

## Testing:
- Ensure that the user input for the exercise is properly passed to the Nutritionix API and that the data returned is valid.
- Verify that the logged data appears correctly in the Google Sheet.
- Handle errors in case the API requests fail or if any parameters are missing.

## Notes:
- You can modify the user profile (weight, height, age) as needed to reflect your actual details.
- Ensure that the Sheety URL and the authentication token are correctly configured to prevent authorization issues.
