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


EMAIL = os.environ["TWITTER_EMAIL"]
PASSWORD = os.environ["TWITTER_PASSWORD"]
USER_ID = os.environ["USER_ID"]



class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_options)
        self.up = os.environ['PROMISED_UP']
        self.down = os.environ['PROMISED_DOWN']
        self.actual_upload = 0
        self.actual_download = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        # Start the speed test
        self.driver.find_element(By.XPATH,
                                 '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()

        try:
            # Wait for the download speed result to appear (up to 120 seconds)
            WebDriverWait(self.driver, 120).until(
                lambda d: d.current_url != "https://www.speedtest.net/"
            )
            # Extract the download speed
            self.actual_download =float(self.driver.find_element(By.CSS_SELECTOR,
                                                            'span.result-data-large.number.result-data-value.download-speed').text)
            self.actual_upload = float(self.driver.find_element(By.CSS_SELECTOR,'span.result-data-large.number.result-data-value.upload-speed').text)
            print(self.actual_download,self.actual_upload)
        except TimeoutException:
            print("Timeout: Speed test took too long or failed to load results.")


    def tweet_at_provider(self):

        # changing the property of the navigator value for webdriver to undefined
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        self.driver.get("https://twitter.com/login")

        # Introduce random delays between actions
        # time.sleep(random.uniform(1, 3))

        # self.driver.find_element(By.LINK_TEXT, "Sign in").click()
        # print("Log In Button clicked")

        # Wait for the email input field
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="text"]'))
        )

        # Introduce random delays between actions
        # time.sleep(random.uniform(1, 3))

        self.driver.find_element(By.CSS_SELECTOR, 'input[name="text"]').send_keys(EMAIL)

        # Wait for the Next button and click it
        # Introduce random delays between actions
        # time.sleep(random.uniform(1, 3))

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//button[contains(@class, "css-175oi2r") and @type="button"]//span[text()="Next"]'))
        ).click()
        print("Next Button clicked")

        # Wait for the password field to appear
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'text'))
            )
            print("User ID field is now visible")
            # Enter the USer ID
            self.driver.find_element(By.NAME, 'text').send_keys(USER_ID)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button/div'))
            )
            self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button/div').click()
        except TimeoutException:
            print("Timeout: Username field did not appear in time")
        except ElementClickInterceptedException:
            print("Message: Element click intercepted")
        try:
            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="password"]'))
            )
            self.driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(PASSWORD)
            self.driver.find_element(By.CSS_SELECTOR,'.css-175oi2r .r-b9tw7p button').click()
        except TimeoutException:
            print("Timeout: Password field did not appear in time")
        except ElementClickInterceptedException:
            print("Message: Log In element click intercepted")

        try:
            tweet_compose = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div'))
            )
            tweet = f"Hey Internet Provider, why is my internet speed {self.actual_download}down/{self.actual_upload}up when I pay for {self.down}down/{self.up}up?"
            tweet_compose.send_keys(tweet)
            time.sleep(3)

            tweet_button = self.driver.find_element(By.XPATH,
                                                    value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
            tweet_button.click()

            time.sleep(5)
            self.driver.quit()

        except NoSuchElementException:
            print("Element hasn't rendered")
        except TimeoutException:
            print("Timeout: Compose field did not appear in time")
        except ElementClickInterceptedException:
            print("Message: Log In element click intercepted")


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
curr_up = bot.actual_upload
curr_down = bot.actual_download

if curr_down < float(bot.down) or curr_up < float(bot.up):
    bot.tweet_at_provider()


