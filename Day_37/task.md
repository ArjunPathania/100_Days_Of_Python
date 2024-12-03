# Task: Pixela API - Track and Manage Reading Data

## Objective:
Create a Python script that interacts with the Pixela API to track your reading progress. You will be able to create an account, create a graph for tracking reading data, log the number of pages read, update the reading progress, and delete specific entries.

## Steps:

### 1. **Set Up the Environment:**
   - Obtain your [Pixela API token](https://pixe.la/) and set it up in the environment variables as `TOKEN`.
   - Set your `USERNAME` for the Pixela account in the environment variables.
   - Install the required libraries using pip:
     ```bash
     pip install requests
     ```

### 2. **Create a Pixela Account (Optional):**
   - Uncomment the code for the account creation if it hasn't been created yet.
   - Use the API to create an account with your username and token. Make sure to agree to the terms of service and verify that you are not a minor.

### 3. **Create a Graph for Tracking Reading Progress:**
   - Create a new graph on Pixela for tracking the number of pages read.
   - The graph should have the following parameters:
     - `id`: A unique identifier for the graph (e.g., `nov2024graph1`).
     - `name`: The name of the activity being tracked (e.g., "Reading").
     - `unit`: The unit of measurement (e.g., "pages").
     - `type`: The type of graph (e.g., `int` for integers).
     - `color`: A color for the graph (e.g., "shibafu").

### 4. **Log Reading Progress:**
   - Use the `pixel_endpt` to log the number of pages read on a specific date.
   - The date should be formatted as `YYYYMMDD` using the `strftime` method. You can set the date to today's date or any date you'd like to track.
   - The `quantity` represents the number of pages read, which should be provided as a string.

### 5. **Update Reading Progress:**
   - You can update the number of pages read for a specific date using the `pixel_update_endpt` endpoint.
   - If needed, you can modify the `quantity` for a particular date.

### 6. **Delete Reading Progress (Optional):**
   - If you need to remove a specific entry, you can use the `pixel_delete_req` endpoint to delete the pixel for that date.
   - This operation will remove the data for the specified date.

## Code Example:

```python
import requests
import os
from datetime import datetime

TOKEN = os.environ.get("TOKEN")
USERNAME = os.environ.get("USERNAME")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Uncomment to create account if not yet created
# account_creation = requests.post(url=pixela_endpoint, json=user_params)
# print(account_creation.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

header = {
    "X-USER-TOKEN": TOKEN
}

graph_parameters = {
    "id": "nov2024graph1",
    "name": "Reading",
    "unit": "pages",
    "type": "int",
    "color": "shibafu"
}

# Uncomment to create graph if not yet created
# graph_create_request = requests.post(url=graph_endpoint, json=graph_parameters, headers=header)
# print(graph_create_request.text)

today = datetime(year=2024, month=11, day=9)

pixel_endpt = f"{pixela_endpoint}/{USERNAME}/graphs/nov2024graph1"

quantity = 10

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": str(quantity)
}

# Uncomment to log reading data
# pixel_req = requests.post(url=pixel_endpt, json=pixel_params, headers=header)
# print(pixel_req.text)

pixel_update_endpt = f"{pixela_endpoint}/{USERNAME}/graphs/nov2024graph1/{today.strftime('%Y%m%d')}"
pixel_update_params = {
    "quantity": str(quantity)
}

# Uncomment to update reading data
# pixel_update_req = requests.put(url=pixel_update_endpt, json=pixel_update_params, headers=header)
# print(pixel_update_req.text)

pixel_delete_req = requests.delete(url=pixel_update_endpt, headers=header)
print(pixel_delete_req.text)
