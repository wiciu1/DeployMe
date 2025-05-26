import logging
from logging import Logger

from selenium import webdriver
from .scraping_manager import ScrapingManager

logger = logging.getLogger(__name__)

class ScrapingEnv:
    def __init__(self, headless=True):
        self.options = webdriver.ChromeOptions()
        if headless:
            self.options.add_argument("--headless")
        self.options.add_argument("--ignore-certificate-errors")
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--incognito')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.driver = self.create_new_driver()

    def create_new_driver(self):
        try:
            return webdriver.Chrome(options=self.options)
        except Exception as e:
            logger.error(f"Failed to create WebDriver: {str(e)}")
            raise RuntimeError("WebDriver initialization failed")

    def reset_driver(self):
        if hasattr(self, 'driver') and self.driver:
            try:
                self.driver.quit()
            except:
                pass
        self.driver = self.create_new_driver()