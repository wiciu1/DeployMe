from abc import ABC, abstractmethod
from selenium import webdriver

class BaseScraper(ABC):
    def __init__(self, headless=True):
        self.options = webdriver.ChromeOptions()
        if headless:
            self.options.add_argument("--headless")
        self.options.add_argument("--ignore-certificate-errors")
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--incognito')

        self.driver = webdriver.Chrome(options=self.options)

    @abstractmethod
    def scrape(self):
        pass

    def quit(self):
        self.driver.quit()

