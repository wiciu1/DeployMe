from abc import ABC, abstractmethod
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver

class BaseScraper(ABC):
    def __init__(self, env):
        self.driver = env.driver
        self.env = env

    @abstractmethod
    def scrape(self, seniority='junior', scrape_iterations=1):
        pass

    def scroll_page(self, container=None, pixels=1000):
        if container:
            self.driver.execute_script("arguments[0].scrollTop += arguments[1];", container, pixels)
        else:
            self.driver.execute_script("window.scrollBy(0, arguments[0]);", pixels)

    def quit(self):
        self.driver.quit()

