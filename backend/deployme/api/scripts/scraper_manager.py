from backend.deployme.api.scripts.jjit_scraper import JJITScraper
from backend.deployme.api.scripts.nfj_scraper import NFJScraper
from backend.deployme.api.scripts.sj_scraper import SJScraper

class ScraperManager:
    def __init__(self):
        self.__scrapers = {
            'JJIT': JJITScraper(headless=False),
            'NFJ': NFJScraper(headless=False),
            'SJ': SJScraper(headless=False)
        }

    def scrape_all(self, seniority="junior", scrape_iterations=1):
        all_offers = []
        for scraper_name, scraper in self.__scrapers.items():
            print(f'Scraping {scraper_name}...')
            try:
                offers = scraper.scrape(seniority=seniority, scrape_iterations=scrape_iterations)
                all_offers.extend(offers)
            except Exception as e:
                print(f'[Error] Scraping {scraper_name}: {str(e)}')
        return all_offers

    def scrape_explicit(self, scraper_name, seniority="junior", scrape_iterations=1):
        all_offers = []
        scraper = self.__scrapers.get(scraper_name)
        if scraper:
            try:
                offers = scraper.scrape(seniority=seniority, scrape_iterations=scrape_iterations)
                all_offers.extend(offers)
            except Exception as e:
                print(f'[Error] Scraping {scraper_name}: {str(e)}')
        return all_offers
