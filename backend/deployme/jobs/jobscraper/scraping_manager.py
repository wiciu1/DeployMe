from .jjit_scraper import JJITScraper
from .nfj_scraper import NFJScraper
from .sj_scraper import SJScraper

import logging
from collections import defaultdict

logger = logging.getLogger(__name__)

class ScrapingManager:
    def __init__(self, env):
        self.scrapers = {
            'NFJ': NFJScraper(env),
            'JJIT': JJITScraper(env),
            'SJ': SJScraper(env)
        }
        self.stats = defaultdict(int)

    def scrape_all(self, seniority='junior', scrape_iterations=1):
        logger.info(f'Started scraping for {seniority} positions')

        for name, scraper in self.scrapers.items():
            try:
                logger.info(f'Running {name} scraper')
                scraper.scrape(seniority, scrape_iterations)
                self.stats[f'{name}_success'] += 1
            except Exception as e:
                logger.error(f'Error running {name} scraper: {str(e)}', exc_info=True)
                self.stats[f'{name}_failure'] += 1

                if hasattr(scraper, 'driver') and scraper.driver:
                    try:
                        scraper.driver.quit()
                    except:
                        pass
                self.env.driver = self.env.create_new_driver()

        return self.stats