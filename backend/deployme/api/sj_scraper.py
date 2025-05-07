from backend.deployme.api.abc_scraper import *


class NFJScraper(ABCScraper):
    def __init__(self):
        super().__init__()
        self.__url = ("https://solid.jobs/api/offers?division=it&sortOrder=salary_desc")

    def scrape(self):
        try:
            response = requests.get(self.__url, headers=self._headers)

            if response.status_code == 200:
                data = response.json()

                for offer in data:
                    offer_data = {
                        'url': f"https://solid.jobs/offer/{offer['id']}/{offer['jobOfferUrl']}",
                        'title': offer['jobTitle'],
                        'seniority': offer['experienceLevel'],
                        'company': offer['companyName'],
                        'location': offer['companyCity'],
                        'salary_from': offer["salaryRange"]["lowerBound"],
                        'salary_to': offer["salaryRange"]["upperBound"],
                        'currency': offer["salaryRange"]["currency"],
                        'tiles': [tile["value"] for tile in offer["requiredSkills"]["name"]]
                    }

                    # Only Junior Data
                    if offer_data['seniority'] == 'Junior':
                        self._junior_offers.append(offer_data)

            else:
                print(f"Error: {response.status_code}")
        except Exception as e:
            print(f"Error: Failed to send request. {e}")