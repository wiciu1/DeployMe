from .jjit_scraper import JJITScraper
from .nfj_scraper import NFJScraper
from .sj_scraper import SJScraper


class ScrapingManager:
    def __init__(self, env):
        self.all_offers = []
        self.junior_offers = []
        self.trainee_offers = []
        self.seen_offers = set() # ID: URL
        self.scrapers = {
            'NFJ': NFJScraper(env),
            'JJIT': JJITScraper(env),
            'SJ': SJScraper(env)
        }

    def add_offer(self, offer, seniority):
        if offer['url'] in self.seen_offers:
            return # just skip, already in
        seniority_lower = seniority.lower()
        if seniority_lower == "trainee":
            self.trainee_offers.append(offer)

        if seniority_lower == "junior":
            self.junior_offers.append(offer)

        self.seen_offers.add(offer['url'])
        self.all_offers.append(offer)

    def scrape_all(self, seniority="junior", scrape_iterations=1):
        for scraper in self.scrapers.values():
            scraper.scrape(seniority, scrape_iterations)