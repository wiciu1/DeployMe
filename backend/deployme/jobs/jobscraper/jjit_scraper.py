from django.db import transaction

from .base_scraper import *
from ..models import Technology, JobOffer


class JJITScraper(BaseScraper):
    BASE_URL = "https://justjoin.it/job-offers/all-locations?"

    def get_scrape_url(self, seniority):
        seniority_map = {
            'junior': 'experience-level=junior',
            'trainee': 'employment-type=internship',
        }
        params = seniority_map.get(seniority, '')
        return f'{self.BASE_URL}{params}&orderBy=DESC&sortBy=published'

    def get_portal_name(self):
        return 'JustJoinIT'

    def _load_more_offers(self):
        self.accept_cookies("cookiescript_accept")
        time.sleep(3)
        self.scroll_page(pixels=2000)
        time.sleep(2)

    def _find_offer_elements(self):
        return self.driver.find_elements(By.CSS_SELECTOR, 'a.offer-card')

    def extract_offer_data(self, offer_element):
        offer_url = offer_element.get_attribute('href')
        title = offer_element.find_element(By.TAG_NAME, 'h3').text
        location = offer_element.find_element(By.CSS_SELECTOR, 'span.css-1o4wo1x').text
        salaries = offer_element.find_elements(By.CSS_SELECTOR, 'div.css-18ypp16 span')

        if len(salaries) >= 3:
            salary = f'{salaries[0].text} - {salaries[1].text} {salaries[2].text}'
        else:
            salary = "undefined"

        skills = offer_element.find_elements(By.CSS_SELECTOR, 'div.MuiBox-root.css-vzlxkq div.css-jikuwi')
        technologies = [skill.text.strip() for skill in skills if skill.text.strip()]

        return {
            'url': offer_url,
            'title': title,
            'location': location,
            'salary': salary,
            'portal': self.get_portal_name(),
            'technologies': technologies
        }
