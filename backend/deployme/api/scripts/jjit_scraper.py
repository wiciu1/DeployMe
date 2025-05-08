from base_scraper import *

class JJITScraper(BaseScraper):
    def __init__(self, env):
        super().__init__(env)
        self.__url = "https://justjoin.it/job-offers/all-locations?"

    def scrape(self, seniority="junior", scrape_iterations=1):
        seniority_map = {
            'junior': 'experience-level=junior',
            'trainee': 'employment-type=internship',
        }
        normalised_seniority = seniority_map.get(seniority, seniority)
        url = self.__url + f'{normalised_seniority}&orderBy=DESC&sortBy=published'

        try:
            self.driver.get(url)

            try:
                cookie_accept = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.ID, "cookiescript_accept")))
                cookie_accept.click()
                time.sleep(3)
            except Exception as e:
                print(f"[ERROR] Cookie Accept did not work: {e}")

            try:
                last_height = self.driver.execute_script("return document.body.scrollHeight")
                offers_container = self.driver.find_element(By.CSS_SELECTOR, '[data-test-id="virtuoso-item-list"]')

                for _ in range(scrape_iterations):
                    self.scroll_page(None, 200)
                    time.sleep(3)

                    offers = offers_container.find_elements(By.CSS_SELECTOR, 'a.offer-card')

                    for offer in offers:

                        offer_url = offer.get_attribute('href')
                        title = offer.find_element(By.TAG_NAME, 'h3').text
                        location = offer.find_element(By.CSS_SELECTOR, 'span.css-1o4wo1x').text
                        salaries = offer.find_elements(By.CSS_SELECTOR, 'div.css-18ypp16 span')
                        if len(salaries) >= 3:
                            salary_min = salaries[0].text
                            salary_max = salaries[1].text
                            currency = salaries[2].text
                            salary = f'{salary_min} - {salary_max} {currency}'
                        else:
                            salary = "Not specified"
                        skill_elements = offer.find_elements(By.CSS_SELECTOR,
                                                             'div.MuiBox-root.css-vzlxkq div.css-jikuwi')

                        skills = [skill.text for skill in skill_elements]

                        offer = ({
                            'seniority': seniority,
                            'url': offer_url,
                            'title': title,
                            'company': '?',
                            'location': location,
                            'salary': salary,
                            'technologies': skills,
                        })

                        self.env.manager.add_offer(offer, seniority.lower())

            except Exception as e:
                print(f"[Error] during parsing data: {str(e)}")

        finally:
            pass