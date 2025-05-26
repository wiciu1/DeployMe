from django.db import transaction

from .base_scraper import *
from ..models import Technology, JobOffer


class NFJScraper(BaseScraper):
    BASE_URL = "https://nofluffjobs.com/pl/?criteria=seniority%3D"

    def get_scrape_url(self, seniority):
        return f"{self.BASE_URL}{seniority}"

    def get_portal_name(self):
        return 'NoFluffJobs'

    def _load_more_offers(self):
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            button = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[nfjloadmore]")))
            self.driver.execute_script("arguments[0].click();", button)
            time.sleep(3)
        except Exception as e:
            logger.debug(f"Could not load more offers: {str(e)}")

    def _find_offer_elements(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "a.posting-list-item")

    def extract_offer_data(self, offer_element):
        offer_url = offer_element.get_attribute("href")
        title = offer_element.find_element(By.CSS_SELECTOR, "h3.posting-title__position").text
        company = offer_element.find_element(By.CSS_SELECTOR, "h4.company-name").text

        try:
            salary = offer_element.find_element(
                By.CSS_SELECTOR,
                "span[data-cy='salary ranges on the job offer listing'].posting-tag").text
            salary = 'undefined' if salary == 'Sprawdź wynagrodzenie' else salary
        except:
            salary = 'undefined'

        location = offer_element.find_element(
            By.CSS_SELECTOR,
            "nfj-posting-item-city[data-cy='location on the job offer listing'] span.tw-text-ellipsis").text

        technologies = [tech.text.strip() for tech in offer_element.find_elements(
            By.CSS_SELECTOR,
            "span[data-cy='category name on the job offer listing'].posting-tag")]

        return {
            'url': offer_url,
            'title': title.replace("NOWA", "").strip(),
            'company': company,
            'location': location,
            'salary': salary,
            'portal': self.get_portal_name(),
            'technologies': technologies
        }