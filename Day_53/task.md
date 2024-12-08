# Task.md  

## **Project Title:**  
**Web Scraping Capstone - Data Entry Job Automation**  

## **Objective:**  
Automate the process of extracting rental property data from Zillow and entering it into a form for organized data collection.  

## **Scope:**  
1. Scrape rental property listings in **San Francisco** from Zillow with the following criteria:  
   - Monthly rent under $3000.  
   - One-bedroom properties.  
2. Clean and organize the extracted data.  
3. Use automation to populate a form with the property details:  
   - Property address.  
   - Monthly rent.  
   - Link to the property.  

---

## **Steps to Completion:**  

### **Phase 1: Web Scraping**
1. **Set Up Environment**  

[//]: # (   - Install required libraries:  )

[//]: # (     ```bash  )

[//]: # (     pip install beautifulsoup4 requests pandas selenium  )

[//]: # (     ```  )

[//]: # (   - Import libraries:)

[//]: # (     ```python  )

[//]: # (     from bs4 import BeautifulSoup  )

[//]: # (     import requests  )

[//]: # (     import pandas as pd  )

[//]: # (     from selenium import webdriver  )

[//]: # (     ```  )

2. **Scrape Zillow Listings**  
   - Send an HTTP GET request to the Zillow website.  
   - Parse the HTML response using BeautifulSoup.  
   - Identify and extract the required data:  
     - Property address.  
     - Monthly rent.  
     - Property link.  

3. **Handle Scraping Challenges**  
   - Implement error handling for missing or inconsistent data fields.  
   - Use headers in the HTTP request to mimic a browser for accessing the site.  

4. **Clean the Data**  
   - Use pandas to organize data into a structured format (e.g., CSV or DataFrame).  
   - Remove duplicate or irrelevant entries.  

---

### **Phase 2: Data Entry Automation**
1. **Set Up Selenium**  
   - Install the browser driver (e.g., ChromeDriver).  
   - Initialize the Selenium WebDriver.  

2. **Automate Form Filling**  
   - Navigate to the form's URL using Selenium.  
   - Locate form fields for address, rent, and property link using appropriate selectors (e.g., `XPath`, `CSS Selectors`).  
   - Populate fields with the cleaned data from the DataFrame.  
   - Submit the form.  

3. **Implement Form Submission Loop**  
   - Use a loop to iterate through all property entries and submit them one by one.  
   - Include delays between submissions to avoid being flagged as a bot.  

---

## **Known Issues and Challenges:**  
- **Web Scraping Challenges:**  
  - Zillow’s dynamic loading may cause partial or missing data.  
  - Use browser headers and simulate user-like behavior to bypass basic bot restrictions.  
- **Selenium Challenges:**  
  - Unexpected pop-ups may interrupt the automation process.  
  - Use exception handling to manage pop-ups.  

---

## **Final Deliverables:**  
- A CSV file containing cleaned property data (address, rent, and link).  
- A Python script that:  
  - Scrapes property data from Zillow.  
  - Automates data entry using Selenium.  
- Demonstration of the working automation process.  

---

## **Required Tools & Libraries:**  
- Python (3.8 or higher).  
- Libraries: BeautifulSoup, Requests, Selenium, Pandas.  
- Browser driver (e.g., ChromeDriver for Selenium).  

---

## **Usage Instructions:**  
1. **Run the Script**  
   - Execute the scraping script to collect data:  
     ```bash  
     python scrape_zillow.py  
     ```  
   - Execute the Selenium script to populate the form:  
     ```bash  
     python fill_form.py  
     ```  

2. **Dependencies**  
   - Ensure all dependencies are installed using the `requirements.txt` file:  
     ```bash  
     pip install -r requirements.txt  
     ```  

---

## **Project Benefits:**  
- Saves time and effort in repetitive data entry tasks.  
- Provides structured, organized data for further analysis or use.  