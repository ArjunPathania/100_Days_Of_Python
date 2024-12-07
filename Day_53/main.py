from scrapper import ZillowScraper
from bot import FormFillerBot

class DataEntryAutomator:
    def __init__(self, scraper):
        self.scraper = scraper
        self.data={}
        self.bot = FormFillerBot()

    def display_data(self):
        self.data = self.scraper.scrape_data()
        print("Links:")
        print("\n".join(self.data["links"]) if self.data["links"] else "No links found.")
        print("\nAddresses:")
        print("\n".join(self.data["addresses"]) if self.data["addresses"] else "No addresses found.")
        print("\nPrices:")
        print("\n".join(self.data["prices"]) if self.data["prices"] else "No prices found.")

    def run(self):
        print("Starting Real Estate Application...")
        self.display_data()
        self.bot.open_form()
        self.bot.fill_answers(self.data)



if __name__ == "__main__":
    scraper = ZillowScraper("ZILLOW")
    app = DataEntryAutomator(scraper)
    app.run()
