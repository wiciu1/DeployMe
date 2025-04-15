from base_scraper import BaseScraper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class NFJScraper(BaseScraper):
    __url = "https://nofluffjobs.com/pl/?criteria=seniority%3Dtrainee,junior"
    all_offers = []
    seen_urls = set()

    def scrape(self, scrape_intervals=3):
        try:
            self.driver.get(self.__url)

            # Accept cookies if they appear
            try:
                cookie_accept = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.ID, "usercentrics-cmp-ui")))
                cookie_accept.find_element(By.CSS_SELECTOR, "button[data-testid='uc-accept-all-button']").click()
                time.sleep(1)
            except:
                pass

            for _ in range(scrape_intervals):
                # Load more offers
                for _ in range(3):
                    try:
                        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                        time.sleep(2)
                        button = WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "button[nfjloadmore]")))
                        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
                        time.sleep(1)
                        self.driver.execute_script("arguments[0].click();", button)
                        time.sleep(3)
                        break
                    except Exception as e:
                        time.sleep(2)

                # Scrape offers
                offers = self.driver.find_elements(By.CSS_SELECTOR, "a.posting-list-item")
                for offer in offers:
                    try:
                        url = offer.get_attribute("href")
                        if url not in self.seen_urls:
                            self.seen_urls.add(url)
                            title = offer.find_element(By.CSS_SELECTOR, "h3.posting-title__position").text
                            company = offer.find_element(By.CSS_SELECTOR, "h4.company-name").text

                            try:
                                salary = offer.find_element(
                                    By.CSS_SELECTOR,
                                    "span[data-cy='salary ranges on the job offer listing'].posting-tag").text
                                if salary == 'Sprawdź wynagrodzenie':
                                    salary = '-'
                            except:
                                salary = '-'

                            location = offer.find_element(
                                By.CSS_SELECTOR,
                                "nfj-posting-item-city[data-cy='location on the job offer listing'] span.tw-text-ellipsis").text

                            technologies = [tech.text.strip() for tech in offer.find_elements(
                                By.CSS_SELECTOR,
                                "span[data-cy='category name on the job offer listing'].posting-tag")]

                            cleaned_title = title.replace("NOWA", "").strip() if title.endswith("NOWA") else title

                            self.all_offers.append({
                                "url": url,
                                "title": cleaned_title,
                                "company": company,
                                "salary": salary,
                                "location": location,
                                "technologies": technologies,
                            })
                    except:
                        continue
        finally:
            self.quit()
        return self.all_offers