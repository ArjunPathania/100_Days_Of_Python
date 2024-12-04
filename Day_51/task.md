# Task: Internet Speed Twitter Bot Development

## Objective
Create a Python automation script that:
1. Tests internet speed using Speedtest.net.
2. Compares actual internet speeds against promised speeds.
3. Posts a complaint on Twitter if the actual speeds are below the promised thresholds.

---

## Key Components

### Environment Setup
- **Libraries:** 
  - `selenium` for browser automation.
  - `dotenv` for environment variable management.
- **Environment Variables (via `.env` file):**
  - `TWITTER_EMAIL`: Twitter login email.
  - `TWITTER_PASSWORD`: Twitter login password.
  - `USER_ID`: Twitter username.
  - `PROMISED_UP`: Promised upload speed.
  - `PROMISED_DOWN`: Promised download speed.

---

### Class: `InternetSpeedTwitterBot`
#### Attributes
- `driver`: Selenium WebDriver instance.
- `up`: Promised upload speed.
- `down`: Promised download speed.
- `actual_upload`: Measured upload speed.
- `actual_download`: Measured download speed.

#### Methods
1. **`__init__`**
   - Initializes the WebDriver with specific Chrome options.

2. **`get_internet_speed`**
   - Opens Speedtest.net.
   - Executes the speed test.
   - Extracts download and upload speeds from the results.

3. **`tweet_at_provider`**
   - Logs into Twitter using the provided credentials.
   - Posts a tweet if the actual speeds are below the promised values.

---

## Steps to Execute
1. **Setup Environment:**
   - Install dependencies:
     ```bash
     pip install selenium python-dotenv
     ```
   - Download and set up the Chrome WebDriver.

2. **Configure `.env` File:**
   - Add the following keys:
     ```
     TWITTER_EMAIL=your_twitter_email
     TWITTER_PASSWORD=your_twitter_password
     USER_ID=your_twitter_username
     PROMISED_UP=10  # example value in Mbps
     PROMISED_DOWN=50  # example value in Mbps
     ```

3. **Run the Script:**
   - Execute the Python script:
     ```bash
     python internet_speed_twitter_bot.py
     ```

4. **Expected Output:**
   - If internet speed is below the threshold:
     - Speedtest results are displayed.
     - A tweet is posted tagging the internet provider with the details.

---

## Troubleshooting
### Common Exceptions and Their Fixes
1. **`TimeoutException`**
   - Ensure stable internet connectivity and increase wait time limits.

2. **`ElementClickInterceptedException`**
   - Verify the UI changes on Speedtest.net or Twitter. Update XPaths/CSS selectors if necessary.

3. **`NoSuchElementException`**
   - Ensure XPaths and CSS selectors match the current website structure.

---

## Future Improvements
1. Add support for other speed-testing websites.
2. Enhance error handling with retries for specific operations.
3. Log activities for monitoring the script’s performance and results.