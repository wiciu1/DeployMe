from abc import ABC, abstractmethod

from django.db import transaction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
import logging

from ..models import Technology, JobOffer

logger = logging.getLogger(__name__)

from tenacity import retry, stop_after_attempt, wait_exponential

class BaseScraper(ABC):
    def __init__(self, env):
        self.driver = env.driver
        self.env = env
        self.wait = WebDriverWait(self.driver, 12)
        self.short_wait = WebDriverWait(self.driver, 5)

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    def _safe_get(self, url):
        self.driver.get(url)
        if "404" in self.driver.title or "Error" in self.driver.title:
            raise ValueError("Page load error detected")

    @abstractmethod
    def get_scrape_url(self, seniority):
        pass

    @abstractmethod
    def get_portal_name(self):
        pass

    @abstractmethod
    def extract_offer_data(self, offer_element):
        pass

    def accept_cookies(self, cookie_locator):
        try:
            cookie_btn = self.short_wait.until(EC.element_to_be_clickable(cookie_locator))
            cookie_btn.click()
            time.sleep(1)
            return True
        except Exception as e:
            logger.debug(f'Cookie acceptance failed: {str(e)}')
            return False

    def scroll_page(self, container=None, pixels=1000):
        try:
            if container:
                self.driver.execute_script("arguments[0].scrollTop += arguments[1];", container, pixels)
            else:
                self.driver.execute_script("window.scrollBy(0, arguments[0]);", pixels)
            time.sleep(1)
        except Exception as e:
            logger.debug(f'Scrolling page failed: {str(e)}')

    def save_offer(self, offer_data):
        try:
            with transaction.atomic():
                technologies = []
                for tech_name in offer_data.get('technologies', []):
                    tech, _ = Technology.objects.get_or_create(name=tech_name)
                    technologies.append(tech)

                offer_obj = JobOffer.objects.create(
                    url = offer_data['url'],
                    title = offer_data['title'],
                    seniority = offer_data['seniority'],
                    company=offer_data.get('company', 'undefined'),
                    location=offer_data.get('location', 'undefined'),
                    salary=offer_data.get('salary', 'undefined'),
                    portal=offer_data['portal'],
                )
                offer_obj.technologies.set(technologies)
                return True

        except Exception as e:
            logger.debug(f'Saving offer failed: {str(e)}')
            return False


    def scrape(self, seniority='junior', scrape_iterations=1):
        url = self.get_scrape_url(seniority)
        try:
            self.driver.get(url)
            for _ in range(scrape_iterations):
                time.sleep(3)
                self._load_more_offers()
                offers = self._find_offer_elements()

                for offer_element in offers:
                    try:
                        offer_data = self.extract_offer_data(offer_element)
                        offer_data['seniority'] = seniority.capitalize()
                        self.save_offer(offer_data)
                    except Exception as e:
                        logger.error(f'Error processing offer: {str(e)}')
                        continue
        except Exception as e:
            logger.error(f'Scraping failed: {str(e)}')
        finally:
            logger.info(f'Completed scraping for {self.__class__.__name__}')

    @abstractmethod
    def _load_more_offers(self):
        pass

    @abstractmethod
    def _find_offer_elements(self):
        pass

    def quit(self):
        self.driver.quit()

