import os
import time

from dotenv import load_dotenv, find_dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

load_dotenv(find_dotenv())

ACCOUNT_EMAIL = os.environ["ACCOUNT_EMAIL"]
ACCOUNT_PASSWORD = os.environ["ACCOUNT_PASSWORD"]
PHONE = os.environ["PHONE_NUMBER"]


def abort_application():
    # Click Close Button
    time.sleep(3)
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(3)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3782263487&f_AL=true&f_E=1%2C2&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILT&spellCorrectionEnab=true")


#sign-in button
time.sleep(5)
sign_in_button = driver.find_element(by=By.CSS_SELECTOR, value='.sign-in-modal button')
sign_in_button.click()
#for sign-in page
# time.sleep(2)
# sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
# sign_in_button.click()

session_key = driver.find_element(By.NAME, value="session_key")
session_password = driver.find_element(By.NAME, value="session_password")
session_key.send_keys(f"{ACCOUNT_EMAIL}")
session_password.send_keys(f"{ACCOUNT_PASSWORD}")
#for log-in page
# time.sleep(5)
# email_field = driver.find_element(by=By.ID, value="username")
# email_field.send_keys(ACCOUNT_EMAIL)
# password_field = driver.find_element(by=By.ID, value="password")
# password_field.send_keys(ACCOUNT_PASSWORD)
# password_field.send_keys(Keys.ENTER)

# CAPTCHA - Solve Puzzle Manually
# input("Press Enter when you have solved the Captcha")

time.sleep(3)
sign_in_btn = driver.find_element(By.CSS_SELECTOR, "#base-sign-in-modal form > div:nth-of-type(2) > button")
# print(f"Is displayed: {sign_in_btn.is_displayed()}")
# print(f"Is enabled: {sign_in_btn.is_enabled()}")
# print(f"Location: {sign_in_btn.location}")
# print(f"Size: {sign_in_btn.size}")
sign_in_btn.click()


time.sleep(3)
easy_apply_btn = driver.find_element(By.CSS_SELECTOR,value=".jobs-apply-button--top-card button")
easy_apply_btn.click()
time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")
# Apply for Jobs

for listing in all_listings:
    print("Opening Listing")
    try:
        # Move to the listing and click it
        ActionChains(driver).move_to_element(listing).click().perform()
        time.sleep(2)  # Allow time for the page to load

        try:
            # Attempt to find and click the Apply button
            apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
            apply_button.click()

            # Insert phone number if required
            time.sleep(5)  # Allow time for input to load
            phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
            if phone.text == "":
                phone.send_keys(PHONE)

            time.sleep(2)

            # Locate and check the submit button
            submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
            if submit_button.text== "Next":
                abort_application()
                print("Complex application, skipped.")
                continue
            else:
                # Submit the application
                print("Submitting job application")
                submit_button.click()

            # Close confirmation modal if present
            time.sleep(2)
            close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
            close_button.click()

        except NoSuchElementException as inner_error:
            # Handle missing application button or other elements
            print(f"Inner error: {inner_error}. Skipping this listing.")
            continue

    except ElementClickInterceptedException as click_error:
        # Handle click interception errors
        print(f"Click intercepted: {click_error}. Skipping this listing.")
        continue

    except Exception as e:
        # Handle any other unexpected errors
        print(f"Error with listing: {e}. Skipping this listing.")
        continue


# for listing in all_listings:
#     print("Opening Listing")
#     driver.execute_script("arguments[0].scrollIntoView(true);", listing)
#     time.sleep(1)  # Allow time for scrolling
#     listing.click()
#     time.sleep(2)
#     try:
#         # Click Apply Button
#         apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
#         apply_button.click()
#
#         # Insert Phone Number
#         time.sleep(5)
#         phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
#         if phone.text == "":
#             phone.send_keys(PHONE)
#
#         # Check the Submit Button
#         submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
#         if submit_button.get_attribute("data-control-name") == "continue_unify":
#             abort_application()
#             print("Complex application, skipped.")
#             continue
#         else:
#             # Click Submit Button
#             print("Submitting job application")
#             submit_button.click()
#
#         time.sleep(2)
#         # Click Close Button
#         close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
#         close_button.click()
#
#     except NoSuchElementException:
#         abort_application()
#         print("No application button, skipped.")
#         continue

time.sleep(5)
driver.quit()
