from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv, find_dotenv


class ZillowScraper:
    def __init__(self, url_env_var):
        load_dotenv(find_dotenv())
        self.url = os.environ.get(url_env_var)
        self.soup = None

    def fetch_html(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            self.soup = BeautifulSoup(response.text, "html.parser")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the URL: {e}")
            self.soup = None

    def extract_links(self):
        if not self.soup:
            return []
        links = self.soup.find_all(name="a", class_="property-card-link")
        return [link.get("href") for link in links if link.get("href")]

    def extract_addresses(self):
        if not self.soup:
            return []
        images = self.soup.select(selector="div picture img")
        return [img.get("alt").replace("|", "").strip() for img in images if img.get("alt")]

    def extract_prices(self):
        if not self.soup:
            return []
        price_elements = self.soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
        return [price.text.split("+")[0].strip() for price in price_elements if price.text]

    def scrape_data(self):
        self.fetch_html()
        if not self.soup:
            return {"links": [], "addresses": [], "prices": []}
        return {
            "links": self.extract_links(),
            "addresses": self.extract_addresses(),
            "prices": self.extract_prices(),
        }
