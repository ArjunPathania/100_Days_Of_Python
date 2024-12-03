```markdown
# Web Scraping and Email Alert Task

## Task Description
This script scrapes the price of a product from Amazon and sends an email alert if the price is below a target threshold.

## Steps to Execute

1. **Load environment variables**: 
   - Use the `dotenv` package to load the `EMAIL_ADDRESS`, `EMAIL_PASSWORD`, and `SMTP_ADDRESS` from an `.env` file.

2. **Send Request to Amazon**: 
   - The script makes a GET request to the Amazon product page URL with a custom `User-Agent` header and cookies.

3. **Parse HTML with BeautifulSoup**: 
   - The response is parsed using BeautifulSoup to extract the product's price.

4. **Extract Price**:
   - Extract the whole price and fraction (if any), calculate the total price.

5. **Check Price and Send Email**:
   - If the total price is below the target (315), an email is sent to the user's email address with a subject and message notifying them of the price drop.

## Requirements

- `requests`: For making the HTTP request to Amazon.
- `beautifulsoup4`: For parsing the HTML response and extracting the price.
- `python-dotenv`: To load environment variables from an `.env` file.
- `smtplib`: To send an email if the price condition is met.

## Example Output

- If the price is below the target, the script will send an email with the following content:

  ```
  Subject: Price Alert

  The product price is now 299.99, below the target price. Buy now!
  ```

## Notes

- Ensure the required environment variables (`EMAIL_ADDRESS`, `EMAIL_PASSWORD`, `SMTP_ADDRESS`) are correctly set in the `.env` file.
- Customize the `URL` variable with the specific Amazon product page URL.
```
