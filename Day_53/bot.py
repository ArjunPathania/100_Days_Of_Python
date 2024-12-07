import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
FORM_URL = os.environ["FORM_LINK"]
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

class FormFillerBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    def open_form(self):
        self.driver.get(FORM_URL)

    def fill_answers(self,data):
        time.sleep(3)
        for _ in range(10):
            self.driver.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(
                data["addresses"][_])
            self.driver.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(
                data["prices"][_])
            self.driver.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(
                data["links"][_])
            self.driver.find_element("xpath", "//span[text()='Submit']").click()
            self.driver.find_element(By.LINK_TEXT,'Submit another response').click()
            time.sleep(3)

