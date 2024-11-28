import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv,find_dotenv
import smtplib

load_dotenv(find_dotenv())

# Making request to amazon
header = {
    "Accept-Language":"en-US,en;q=0.9,hi;q=0.8",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}
URL="https://www.amazon.in/Paperkraft-Vintage-Color-Unruled-Perfect/dp/B0B34H5QJC/?_encoding=UTF8&pd_rd_w=sVjny&content-id=amzn1.sym.87086214-159f-48ce-bbbc-e0bf66cd937f%3Aamzn1.symc.9b8fba90-e74e-4690-b98f-edc36fe735a6&pf_rd_p=87086214-159f-48ce-bbbc-e0bf66cd937f&pf_rd_r=3E82ZQG1CVWE3J8SV9JN&pd_rd_wg=DuXNn&pd_rd_r=abaea056-cf55-4606-9233-eb1bd76a99ea&ref_=pd_hp_d_btf_ci_mcx_mr_ca_id_hp_d"

cookies = {
    "AMCV_7742037254C95E840A4C98A6%40AdobeOrg": "",
    "csm-hit": "",
    "i18n-prefs": "",
    "sess-at-acbin": "",
    "sess-at-main": "",
    "session-id": "",
    "session-id-time": "",
    "session-token": "",
    "ubid-acbin": "",
}


response = requests.get(url=URL,cookies=cookies,headers=header)
response.raise_for_status()

# Creating Soup
soup = BeautifulSoup(response.text,"html.parser")
print(soup.prettify())

# Extract the whole price
whole_price_element = soup.find(name="span", class_="a-price-whole")
if whole_price_element:
    whole_price = float(whole_price_element.text.replace(',', '').strip())
else:
    raise ValueError("Whole price element is missing, but it's expected to exist.")

# Extract the fraction price (optional)
fraction_price_element = soup.find(name="span", class_="a-price-fraction")
fraction_price = float(fraction_price_element.text.strip()) / 100 if fraction_price_element else 0

# Calculate total price
total_price = whole_price + fraction_price

print(f"Whole price: {whole_price}, Fraction price: {fraction_price}, Total price: {total_price}")


EMAIL = os.environ["EMAIL_ADDRESS"]
PASSWORD = os.environ["EMAIL_PASSWORD"]
SMTP_ADDRESS=os.environ["SMTP_ADDRESS"]

if total_price<315:
    try:
        with smtplib.SMTP(SMTP_ADDRESS, 587) as connection:
            connection.starttls()  # Secure the connection
            connection.login(EMAIL, PASSWORD)
            # Now you can send an email
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=f"Subject:Price Alert\n\nThe product price is now {total_price},below target price. Buy now !"
            )
            print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
