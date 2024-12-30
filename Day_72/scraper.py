from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import sleep
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.google.com/',
    'Connection': 'keep-alive'
}

data_dict = {
    'Rank': [],
    'Major': [],
    'Degree': [],
    'Early Career Pay': [],
    'Mid Career Pay': [],
    'Percent High Meaning': [],
}

def fetch_page(url, retries=3):
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            sleep(2)
    print(f"Failed to fetch {url} after {retries} attempts.")
    return None


for page in range(1, 33):
    print(f"Fetching page {page}...")
    url = f'https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{page}'
    web_page = fetch_page(url)

    if web_page is None:
        print(f"Skipping page {page} due to repeated fetch failures.")
        continue

    soup = BeautifulSoup(web_page, "html.parser")
    all_values = soup.find_all(name="span", class_='data-table__value')

    i = 0
    for value in all_values:
        text = value.get_text().strip()
        i += 1
        if i == 1:
            data_dict['Rank'].append(text)
        elif i == 2:
            data_dict['Major'].append(text)
        elif i == 3:
            data_dict['Degree'].append(text)
        elif i == 4:
            data_dict['Early Career Pay'].append(int(text.replace('$', '').replace(',', '')) if text else None)
        elif i == 5:
            data_dict['Mid Career Pay'].append(int(text.replace('$', '').replace(',', '')) if text else None)
        elif i == 6:
            try:
                data_dict['Percent High Meaning'].append(int(text.strip('%')) if text else None)
            except ValueError:
                data_dict['Percent High Meaning'].append(None)
        if i == 6:
            i = 0


all_data = pd.DataFrame(data_dict)

if os.path.exists('all_data_new.csv'):
    print("File 'all_data.csv' already exists.")
else:
    all_data.to_csv('all_data.csv', index=False)
    print("Data saved to 'all_data.csv'.")
