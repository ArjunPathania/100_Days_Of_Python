from selenium import webdriver
from selenium.webdriver.common.by import By

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize the Chrome driver
driver = webdriver.Chrome(options=chrome_options)

# Open Amazon website
driver.get("https://www.amazon.in/Pigeon-Electric-Stainless-Shut-off-Feature/dp/B07WMS7TWB/?_encoding=UTF8&pd_rd_w=wdcnY&content-id=amzn1.sym.211684f4-ebe1-443f-8a4a-0773471e979f&pf_rd_p=211684f4-ebe1-443f-8a4a-0773471e979f&pf_rd_r=FZH141PTZN0E9XJR1W4J&pd_rd_wg=uOdzZ&pd_rd_r=7be198c2-cca6-498e-abc5-0d6239b3403d&ref_=pd_hp_d_btf_crs_zg_bs_976442031")

price_whole = driver.find_element(By.CLASS_NAME,"a-price-whole")
print(f"The price is {price_whole.text}")

driver.quit()