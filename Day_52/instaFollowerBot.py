import random
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
import os
from dotenv import load_dotenv, find_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv(find_dotenv())

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# adding argument to disable the AutomationControlled flag
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# exclude the collection of enable-automation switches
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# turn-off userAutomationExtension
chrome_options.add_experimental_option("useAutomationExtension", False)

USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']
SIMILAR_ACCOUNT=os.environ['SIMILAR_ACCOUNT']

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_options)

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/?hl=en')
        try:
            WebDriverWait(self.driver,5).until(
                EC.presence_of_element_located((By.NAME,'username'))
            )
            self.driver.find_element(By.NAME,'username').send_keys(USERNAME)
            self.driver.find_element(By.NAME,"password").send_keys(PASSWORD)
        except NoSuchElementException:
            print("Username Field Not Detected")
        except TimeoutException:
            print("Timeout: Username took too ong to load")

        try:
            self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div').click()
        except ElementClickInterceptedException:
            print("Login button click intercepted")
        except NoSuchElementException:
            print("Log In button Not detected")

    def find_followers(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'div svg[aria-label="Search"]'))
            ).click()
            self.driver.find_element(By.CSS_SELECTOR,'div input[aria-label="Search input"]').send_keys(SIMILAR_ACCOUNT)
            self.driver.find_element(By.CSS_SELECTOR, 'div input[aria-label="Search input"]').send_keys()
        except NoSuchElementException:
            print("Search Field Not Detected")
        except TimeoutException:
            print("Timeout: Search field took too Long to load")
            try:
                element = self.driver.find_element(By.CSS_SELECTOR, 'div svg[aria-label="Search"]')
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                print("Search scrolled")
                element.click()
            except ElementClickInterceptedException:
                print("search element click intercepted")
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"a[href='/{SIMILAR_ACCOUNT}/']"))
            ).click()
        except ElementClickInterceptedException:
            print("search element click intercepted")
        except NoSuchElementException:
            print("Link Not Detected")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"ul li div a[href='/{SIMILAR_ACCOUNT}/followers/?hl=en']"))
            ).click()
        except ElementClickInterceptedException:
            print("Follower element click intercepted")
        except NoSuchElementException:
            print("Follower Element Not Detected")

        for i in range(10):
            elm = self.driver.find_element(By.XPATH,
                                           "/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]")
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", elm)
            time.sleep(random.randint(500, 1000) / 1000)

    def follow(self):
        follow_buttons = self.driver.find_elements(By.XPATH, '//div[contains(text(), "Follow")]')
        for follow in follow_buttons:
            if follow.text == "Following":
                time.sleep(1)
                print(follow.text)
            elif follow.text == "Requested":
                time.sleep(1)
                print(follow.text)



bot = InstaFollower()
bot.login()
bot.find_followers()