from base_scraper import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SJScraper(BaseScraper):
    url = 'https://solid.jobs/offers/it/'
    seen_urls = set()

    def scrape(self, seniority='junior', scrape_iterations=1):
        offers_data = []

        seniority_map = {
            'trainee': 'Staż',
            'junior': 'Junior'
        }
        normalized_seniority = seniority_map.get(seniority, seniority)

        base_url = f'https://solid.jobs/offers/it;experiences={normalized_seniority}'
        self.driver.get(base_url)

        try:
            scroll_container = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.TAG_NAME, 'virtual-scroller'))
            )

            for _ in range(scrape_iterations):
                self.scroll_page(scroll_container, 1000);
                time.sleep(1)

            offers = self.driver.find_elements(By.CSS_SELECTOR, "sj-offer-list-item")
            for offer in offers:
                try:
                    offer_url = offer.find_element(By.CSS_SELECTOR, "a.card.py-2").get_attribute('href')
                    if offer_url not in self.seen_urls:
                        self.seen_urls.add(offer_url)
                        title = offer.find_element(By.CSS_SELECTOR, "h2 a").text.strip()

                        company = offer.find_element(By.XPATH, "//a[@mattooltip='Kliknij, aby zobaczy pozostałe oferty firmy.']").find_element(By.CSS_SELECTOR, "span").text
                        location = offer.find_element(By.XPATH, "//span[@mattooltip='Kliknij, aby zobaczyć inne oferty z okolicy.']").text.split(',')[-1].strip()
                        salary = offer.find_element(By.CSS_SELECTOR, "sj-salary-display").text.strip()
                        technologies = [
                            tech.text.strip('#')
                            for tech in offer.find_elements(By.CSS_SELECTOR, "solidjobs-skill-display")
                        ]

                        print(offer_url, title, company, location, salary, technologies)

                        offers_data.append({
                            'url': offer_url,
                            'title': title,
                            'company': company,
                            'location': location,
                            'salary': salary,
                            'technologies': technologies
                        })

                except Exception as e:
                    print(f"[Error] during parsing data {e}")

        finally:
            pass
        return offers_data
