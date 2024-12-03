```markdown
# Tinder Automation Bot Task

## Task Description
This script automates the process of logging into Tinder using Facebook credentials, entering a phone number, and performing actions such as "Liking" profiles. It also handles various elements such as popups and Captcha manually.

## Steps to Execute

1. **Load Environment Variables**:
   - Use the `dotenv` package to load the following environment variables from an `.env` file:
     - `URL`: The Tinder login URL.
     - `EMAIL`: Facebook email for login.
     - `PASSWORD`: Facebook password for login.
     - `PHONE`: Phone number for account verification.

2. **Configure Logging**:
   - The script uses the `logging` module to log information and errors throughout the process.

3. **Initialize WebDriver**:
   - A Chrome WebDriver is initialized and opens the Tinder URL provided in the `.env` file.

4. **Click the Login Button**:
   - Wait for and click the Tinder "Login" button.

5. **Handle Facebook Login**:
   - If the Facebook login button is visible, it will click it; if not, it will reveal additional options and click the Facebook login button.
   
6. **Switch to New Window for Facebook Authentication**:
   - The script switches to the new browser window that opens for Facebook login.

7. **Facebook Authentication**:
   - It enters Facebook credentials (email and password) into the login fields and clicks the login button.

8. **Click 'Continue as' Button**:
   - After logging into Facebook, it clicks the "Continue as" button to allow Tinder to access the account.

9. **Switch Back to Main Window**:
   - After Facebook authentication, it switches back to the Tinder main window.

10. **Enter Phone Number**:
    - It enters the phone number from the `.env` file into the phone number field and clicks the "Next" button.

11. **Manual CAPTCHA and OTP Entry**:
    - Wait for the user to manually solve the CAPTCHA and enter the OTP.

12. **Allow Location and Notifications**:
    - Clicks the buttons to allow location and disallow notifications.

13. **Allow Cookies**:
    - Clicks the button to accept cookies.

14. **Perform Likes**:
    - The script automatically likes up to 100 profiles, with a 1-second delay between each like.
    - It handles pop-ups when a match occurs and retries if the "Like" button has not yet loaded.

15. **Error Handling**:
    - The script handles various exceptions, such as timeouts, element not found, or click interception, and logs any issues that arise.

## Requirements

- `selenium`: For automating the browser.
- `time`: For managing delays between actions.
- `os` and `dotenv`: For loading sensitive account information from environment variables.
- `logging`: For error and status logging.

## Example Output

- The script will log messages like:
  ```
  INFO - Login button clicked successfully.
  INFO - Facebook login credentials entered.
  INFO - 'Continue as' button clicked.
  INFO - Phone number entered.
  INFO - 'Like' button clicked.
  INFO - Process completed.
  ```

## Notes

- The script requires manual CAPTCHA solving and OTP entry by the user.
- Ensure the necessary environment variables (`URL`, `EMAIL`, `PASSWORD`, `PHONE`) are set in a `.env` file.
- This script is designed to like up to 100 profiles per day due to Tinder's limitations on the free tier.
- It includes error handling to manage various exceptions that may arise during automation.

## Improvements

- Consider adding more robust error handling and retries for complex scenarios like Captcha failures.
- Extend the script to support premium users with more likes per day by using a while loop.
```