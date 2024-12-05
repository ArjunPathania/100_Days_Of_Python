import random
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
)
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
SIMILAR_ACCOUNT = os.environ["SIMILAR_ACCOUNT"]


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)


class InstaFollower:
    def __init__(self):

        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        """
        Logs into Instagram using provided credentials.
        """
        self.driver.get("https://www.instagram.com/accounts/login/?hl=en")
        try:

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            self.driver.find_element(By.NAME, "username").send_keys(USERNAME)
            self.driver.find_element(By.NAME, "password").send_keys(PASSWORD)


            self.driver.find_element(
                By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div'
            ).click()
            print("Login attempt successful.")
        except TimeoutException:
            print("Timeout: Login page elements took too long to load.")
        except NoSuchElementException as e:
            print(f"Error during login: {e}")

    def find_followers(self):
        """
        Navigates to the target account and scrolls through its followers.
        """
        try:

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'div svg[aria-label="Search"]'))
            ).click()


            search_input = self.driver.find_element(By.CSS_SELECTOR, 'div input[aria-label="Search input"]')
            search_input.send_keys(SIMILAR_ACCOUNT)
            time.sleep(2)

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"a[href='/{SIMILAR_ACCOUNT}/']"))
            ).click()


            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, f"ul li div a[href='/{SIMILAR_ACCOUNT}/followers/?hl=en']")
                )
            ).click()

            print(f"Navigated to {SIMILAR_ACCOUNT}'s followers list.")

            time.sleep(3)
        except Exception as e:
            print(f"Error during find_followers: {e}")

    def follow(self):
        """
        Clicks the 'Follow' button for each follower in the modal.
        """
        try:
            modal_xpath = "/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]"
            modal = self.driver.find_element(By.XPATH, modal_xpath)

            for _ in range(10):
                try:
                    follow_buttons = self.driver.find_elements(
                        By.XPATH, '//button[contains(@class, "_acan") and .//div[text()="Follow"]]'
                    )
                    for button in follow_buttons:
                        try:
                            button.click()
                            print("Followed a user.")
                            time.sleep(random.uniform(2, 4))
                        except ElementClickInterceptedException:
                            print("Follow button click intercepted. Attempting to click 'OK' button.")
                            try:

                                ok_button = self.driver.find_element(By.XPATH,
                                                                     '//button[contains(@class, "_a9--") and text()="OK"]')
                                ok_button.click()
                                print("Clicked 'OK' button.")
                                time.sleep(2)
                            except NoSuchElementException:
                                print("'OK' button not found. Skipping user.")
                            except Exception as e:
                                print(f"Error clicking 'OK' button: {e}")
                        except Exception as e:
                            print(f"Error clicking follow button: {e}")

                    # Scroll the modal
                    self.driver.execute_script(
                        "arguments[0].scrollTop = arguments[0].scrollHeight", modal
                    )
                    time.sleep(random.uniform(2, 4))
                except StaleElementReferenceException:
                    print("Stale element detected. Re-fetching modal.")
                    modal = self.driver.find_element(By.XPATH, modal_xpath)
        except Exception as e:
            print(f"Error during follow: {e}")

    def close_browser(self):
        """
        Closes the WebDriver instance.
        """
        self.driver.quit()

if __name__ == "__main__":
    bot = InstaFollower()
    bot.login()
    time.sleep(5)
    bot.find_followers()
    bot.follow()
    bot.close_browser()
