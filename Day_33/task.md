# Task.md: ISS Tracker and Notification System

## **Project Overview**
This project tracks the position of the International Space Station (ISS) and sends an email notification when it is visible in the night sky from a specified location. The program uses the ISS API to determine the station's position, the Sunrise-Sunset API to check local nighttime hours, and SMTP for email notifications.

---

## **Features and Functionality**

### 1. **ISS Position Tracking**
   - Queries the ISS location using the `http://api.open-notify.org/iss-now.json` API.
   - Checks if the ISS is within ±5 degrees of the user's latitude and longitude.

### 2. **Nighttime Detection**
   - Queries the `https://api.sunrise-sunset.org/json` API to get sunrise and sunset times for the user's location.
   - Determines if it is currently nighttime based on the local time and sunset/sunrise data.

### 3. **Email Notification**
   - Sends an email alert when the ISS is visible during nighttime hours.
   - Uses Gmail's SMTP server for secure email delivery.

---

## **Project File Structure**

| **File/Folder**  | **Description**                                      |
|------------------|------------------------------------------------------|
| `iss_tracker.py` | Main script for ISS tracking and email notification. |
| `secrets.json`   | Stores email credentials securely.                   |

---

## **Core Logic**

### 1. **Position Check**
   - Queries the ISS position API:

[//]: # (     ```python)

[//]: # (     response = requests.get&#40;url="http://api.open-notify.org/iss-now.json"&#41;)

[//]: # (     ```)
   - Parses the latitude and longitude of the ISS and checks proximity to the user’s location:

[//]: # (     ```python)

[//]: # (     if &#40;MY_LAT - 5 <= iss_latitude <= MY_LAT + 5&#41; and &#40;MY_LONG - 5 <= iss_longitude <= MY_LONG + 5&#41;:)

[//]: # (         return True)

[//]: # (     ```)

### 2. **Nighttime Check**
   - Queries the Sunrise-Sunset API with the user’s coordinates:

[//]: # (     ```python)

[//]: # (     parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0})

[//]: # (     response = requests.get&#40;"https://api.sunrise-sunset.org/json", params=parameters&#41;)

[//]: # (     ```)
   - Parses sunrise and sunset times and compares them to the current hour.

### 3. **Email Notification**
   - Sends an email alert when both conditions (ISS proximity and nighttime) are true:

[//]: # (     ```python)

[//]: # (     with smtplib.SMTP&#40;"smtp.gmail.com", 587&#41; as connection:)

[//]: # (         connection.starttls&#40;&#41;)

[//]: # (         connection.login&#40;user=my_email, password=password&#41;)

[//]: # (         connection.sendmail&#40;from_addr=my_email, to_addrs=my_email, msg=f"Subject:Look Up\n\nTry to find the ISS in the night sky"&#41;)

[//]: # (     ```)

---

## **Setup and Execution**

### 1. **Install Python and Dependencies**
   - Ensure Python is installed.
   - Install required libraries:
     ```bash
     pip install requests
     ```

### 2. **Configure Secrets**
   - Create a `secrets.json` file in the following format:
     ```json
     {
       "accounts": [
         {
           "email": "your_email@gmail.com",
           "password": "your_password"
         }
       ]
     }
     ```

### 3. **Run the Script**
   ```bash
   python iss_tracker.py
   ```

---

## **API Details**

### 1. **ISS Position API**
   - **URL**: `http://api.open-notify.org/iss-now.json`
   - **Method**: `GET`
   - **Response**:
     ```json
     {
       "timestamp": 1598067437,
       "iss_position": {
         "latitude": "32.205",
         "longitude": "75.707"
       },
       "message": "success"
     }
     ```

### 2. **Sunrise-Sunset API**
   - **URL**: `https://api.sunrise-sunset.org/json`
   - **Method**: `GET`
   - **Parameters**:
     - `lat`: Latitude of the location.
     - `lng`: Longitude of the location.
     - `formatted`: `0` for ISO 8601 response.
   - **Response**:
     ```json
     {
       "results": {
         "sunrise": "2024-12-03T01:47:00+00:00",
         "sunset": "2024-12-03T14:47:00+00:00"
       },
       "status": "OK"
     }
     ```

---

## **Enhancements To-Do**

1. **Geolocation Automation**
   - Automatically fetch the user’s latitude and longitude using IP geolocation services.

2. **Retry Logic**
   - Add retries for API requests in case of transient failures.

3. **Mobile Notifications**
   - Use Twilio API to send SMS alerts as an alternative to email.

4. **Improved Proximity Detection**
   - Allow users to customize the proximity range for ISS visibility.

5. **Multi-user Support**
   - Add support for sending notifications to multiple recipients.

---
