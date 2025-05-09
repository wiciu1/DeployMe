from selenium import webdriver
from .scraping_manager import ScrapingManager

class ScrapingEnv:
    def __init__(self, headless=True):
        self.options = webdriver.ChromeOptions()
        if headless:
            self.options.add_argument("--headless")
        self.options.add_argument("--ignore-certificate-errors")
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--incognito')

        self.driver = webdriver.Chrome(options=self.options)
        self.manager = None

    def set_manager(self, manager):
        self.manager = manager

    def quit(self):
        self.driver.quit()