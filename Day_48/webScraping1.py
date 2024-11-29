from selenium import webdriver
from selenium.webdriver.common.by import By

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org/")

event_dates = driver.find_elements(By.CSS_SELECTOR,value=".event-widget li time")
event_names = driver.find_elements(By.CSS_SELECTOR,value=".event-widget li a")


events = {
    number: {
        "date": event_dates[number].text,
        "name": event_names[number].text
    }
    for number in range(len(event_dates))
}
print(events)


driver.quit()
