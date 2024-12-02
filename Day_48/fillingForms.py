from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options = chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

fName = driver.find_element(By.NAME,value="fName")
fName.send_keys("arjun")

lName = driver.find_element(By.NAME,value="lName")
lName.send_keys("pathania")

email = driver.find_element(By.NAME,value="email")
email.send_keys("arjunpathania@gmail.com")

submit = driver.find_element(By.CLASS_NAME,value="btn-lg")
submit.click()

driver.quit()