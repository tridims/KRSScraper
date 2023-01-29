from config import DEFAULT_CONFIGURATION, DEFAULT_PAYLOADS
from scraper import KRSScraper

if __name__ == "__main__":
    scraper = KRSScraper(DEFAULT_CONFIGURATION, DEFAULT_PAYLOADS)
    result = scraper.scrape()

    print(result)
    scraper.save("result.csv")
