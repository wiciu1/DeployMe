from django.db import transaction

from .base_scraper import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..models import Technology, JobOffer


class SJScraper(BaseScraper):
    BASE_URL = "https://solid.jobs/offers/it;experiences="

    def get_scrape_url(self, seniority):
        seniority_map = {
            'trainee': 'Staż',
            'junior': 'Junior'
        }
        return f"{self.BASE_URL}{seniority_map.get(seniority, seniority)}"

    def get_portal_name(self):
        return 'SolidJobs'

    def _load_more_offers(self):
        scroll_container = self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, 'virtual-scroller')))
        self.scroll_page(scroll_container, 1000)
        time.sleep(1)

    def _find_offer_elements(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "sj-offer-list-item")

    def extract_offer_data(self, offer_element):
        time.sleep(3)
        offer_url = offer_element.find_element(By.CSS_SELECTOR, "a.card.py-2").get_attribute('href')
        title = offer_element.find_element(By.CSS_SELECTOR, "h2 a").text.strip()
        company = offer_element.find_element(
            By.XPATH, "//a[@mattooltip='Kliknij, aby zobaczy pozostałe oferty firmy.']//span").text
        location = offer_element.find_element(
            By.XPATH, "//span[@mattooltip='Kliknij, aby zobaczyć inne oferty z okolicy.']").text.split(',')[-1].strip()
        salary = offer_element.find_element(By.CSS_SELECTOR, "sj-salary-display").text.strip()

        tech_elements = offer_element.find_elements(By.CSS_SELECTOR, "solidjobs-skill-display")
        technologies = [tech.text.strip('#').strip() for tech in tech_elements if tech.text.strip()]

        return {
            'url': offer_url,
            'title': title,
            'company': company,
            'location': location,
            'salary': salary,
            'portal': self.get_portal_name(),
            'technologies': technologies
        }
