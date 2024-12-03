# Task.md: Automated Birthday Email Sender

## **Project Overview**
This project automates sending personalized birthday emails. It uses a CSV file to track birthdays, dynamically selects an email template, and sends customized birthday wishes via Gmail's SMTP server.

---

## **Features and Functionality**

### 1. **Birthday Detection**
   - Reads birthday data from `birthdays.csv`.
   - Checks the current date against birthdays in the file.
   - Supports multiple recipients with birthdays on the same day.

### 2. **Email Customization**
   - Uses placeholders (`[NAME]`) in email templates.
   - Dynamically replaces placeholders with recipient names.
   - Selects one of three predefined templates randomly.

### 3. **Secure Email Sending**
   - Utilizes Gmail's SMTP server for sending emails.
   - Ensures secure login using credentials stored in a `secrets.json` file.

### 4. **Logging and Error Handling**
   - Prints a success message upon successful email delivery.
   - Captures and logs errors during email sending.

---

## **Project File Structure**

| **File/Folder**            | **Description**                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| `birthdays.csv`            | Stores recipient names, emails, and birthdays.                                         |
| `letter_templates/`        | Contains pre-written email templates (`letter_1.txt`, `letter_2.txt`, `letter_3.txt`). |
| `secrets.json`             | Stores email credentials securely.                                                     |
| `birthday_email_sender.py` | Main script for detecting birthdays and sending emails.                                |

---

## **Data Handling**

### 1. **CSV File (`birthdays.csv`)**
   - Structure:
     ```csv
     name,email,year,month,day
     John Doe,johndoe@gmail.com,1990,12,3
     Jane Smith,janesmith@gmail.com,1985,7,15
     ```
   - Columns:
     - `name`: Recipient's name.
     - `email`: Recipient's email address.
     - `year`, `month`, `day`: Date of birth.

### 2. **Email Templates (`letter_templates/`)**
   - Example format:
     ```
     Dear [NAME],

     Wishing you a very Happy Birthday! Have an amazing day filled with joy and laughter.

     Best,
     Your Friends
     ```

### 3. **Secrets File (`secrets.json`)**
   - Structure:
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

---

## **Core Functions**

| **Functionality**      | **Description**                                                           |
|------------------------|---------------------------------------------------------------------------|
| **Birthday Matching**  | Checks if today's date matches any birthdays in `birthdays.csv`.          |
| **Template Selection** | Picks a random template from the `letter_templates/` folder.              |
| **Personalization**    | Replaces `[NAME]` in the template with the recipient's name.              |
| **Email Sending**      | Sends the personalized email via Gmail's SMTP server.                     |
| **Error Handling**     | Logs errors if email sending fails and continues with the next recipient. |

---

## **Setup and Execution**

1. **Install Python and Dependencies**
   - Ensure Python is installed.
   - Install required libraries:
     ```bash
     pip install pandas
     ```

2. **Configure Files**
   - Add birthdays to `birthdays.csv`.
   - Place templates in the `letter_templates/` folder.
   - Create a `secrets.json` file with your Gmail credentials.

3. **Run the Script**
   ```bash
   python birthday_email_sender.py
   ```

---

## **Enhancements To-Do**

1. **Email Preview**
   - Display the email content for confirmation before sending.

2. **Multiple SMTP Providers**
   - Add support for other email providers (e.g., Yahoo, Outlook).

3. **Scheduling**
   - Use a scheduler (e.g., `cron` or `schedule` library) to run the script daily.

4. **Mobile Integration**
   - Send SMS or WhatsApp messages as an alternative.

5. **Enhanced Security**
   - Use OAuth 2.0 for Gmail instead of plain-text credentials.

---