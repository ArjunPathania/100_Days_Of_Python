import logging
import os
import time
from dotenv import load_dotenv, find_dotenv
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Load environment variables
load_dotenv(find_dotenv())
required_env_vars = ["URL", "EMAIL", "PASSWORD", "PHONE"]
for var in required_env_vars:
    if var not in os.environ:
        raise ValueError(f"Environment variable {var} is not set.")

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.get(os.environ["URL"])

def click_element(wait, locator, description):
    """
    Helper function to wait for and click an element.
    """
    try:
        element = wait.until(EC.element_to_be_clickable(locator))
        element.click()
        logging.info(f"{description} clicked successfully.")
        return element
    except TimeoutException:
        logging.error(f"Timeout: Unable to click {description}.")
        return None

def switch_to_new_window(driver, main_window):
    """
    Switch to a new browser window.
    """
    try:
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
        for window in driver.window_handles:
            if window != main_window:
                driver.switch_to.window(window)
                logging.info("Switched to the new window.")
                return True
    except TimeoutException:
        logging.error("No new window detected for Facebook login.")
    return False

def switch_back_to_main_window(driver, main_window):
    """
    Switch back to the main browser window.
    """
    try:
        driver.switch_to.window(main_window)
        logging.info("Switched back to the main window.")
    except Exception as e:
        logging.error(f"Failed to switch back to the main window: {e}")

def login_facebook(driver, email, password):
    """
    Perform login on Facebook's window.
    """
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(email)
        driver.find_element(By.ID, "pass").send_keys(password)
        driver.find_element(By.NAME, "login").click()
        logging.info("Facebook login credentials entered.")
    except NoSuchElementException:
        logging.error("Failed to find Facebook login fields.")

def enter_phone_number(driver, phone):
    """
    Enter the phone number and click the 'Next' button.
    """
    try:
        phone_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "phone_number")))
        phone_field.send_keys(phone)
        logging.info("Phone number entered.")
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[text()="Next"]')))
        next_button.click()
        logging.info("'Next' button clicked.")
    except TimeoutException:
        logging.error("Failed to enter phone number or click 'Next'.")

try:
    wait = WebDriverWait(driver, 10)

    # Step 1: Click Login button
    click_element(wait,
                  (By.XPATH, '//*[@id="q807713831"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div'),
                  "Login button")

    # Step 2: Handle Facebook Login
    try:
        facebook_login = click_element(wait,
                                       (By.XPATH, '//*[@id="q-920667245"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]'),
                                       "Facebook login button")
        if not facebook_login:
            logging.info("Facebook login not directly visible. Clicking 'More Options'.")
            more_options = click_element(wait,
                                          (By.XPATH, '//*[@id="q-920667245"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/button'),
                                          "'More Options'")
            if more_options:
                facebook_login = click_element(wait,
                                               (By.XPATH, '//*[@id="q-920667245"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]'),
                                               "Facebook login button after revealing it")
    except Exception as e:
        logging.error(f"An error occurred while handling Facebook login: {e}")

    # Step 3: Switch to new window for Facebook authentication
    main_window = driver.current_window_handle
    if switch_to_new_window(driver, main_window):
        login_facebook(driver, os.environ["EMAIL"], os.environ["PASSWORD"])

    # Step 4: Click "Continue as" button
    try:
        continue_as_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Continue as')]"))
        )
        continue_as_button.click()
        logging.info("'Continue as' button clicked.")
    except TimeoutException:
        logging.error("Failed to locate 'Continue as' button.")

    # Step 4.1: Switch back to the main window
    switch_back_to_main_window(driver, main_window)

    # Step 5: Enter phone number
    enter_phone_number(driver, os.environ["PHONE"])

    input("Press Enter after Solving Captch and Enter OTP")

    # Allow location
    allow_location_button = driver.find_element(By.XPATH,
                                                value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
    allow_location_button.click()

    # Disallow notifications
    notifications_button = driver.find_element(By.XPATH,
                                               value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
    notifications_button.click()

    # Allow cookies
    cookies = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
    cookies.click()

    # Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
    for n in range(100):
        # Add a 1 second delay between likes.
        time.sleep(1)
        try:
            print("called")
            like_button = driver.find_element(By.XPATH, value=
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
            like_button.click()

        # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
        except ElementClickInterceptedException:
            try:
                match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
                match_popup.click()

            # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
            except NoSuchElementException:
                time.sleep(2)


except Exception as e:
    logging.error(f"An unexpected error occurred: {e}")
finally:
    logging.info("Process completed.")
