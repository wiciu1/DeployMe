from backend.deployme.api.scripts.jjit_scraper import JJITScraper
from backend.deployme.api.scripts.nfj_scraper import NFJScraper
from backend.deployme.api.scripts.scraping_env import ScrapingEnv
from backend.deployme.api.scripts.scraping_manager import ScrapingManager
from backend.deployme.api.scripts.sj_scraper import SJScraper
env = ScrapingEnv(headless=False)
manager = ScrapingManager(env)
env.set_manager(manager)
manager.scrape_all()
for offer in manager.junior_offers:
    print(offer)

env.quit()
