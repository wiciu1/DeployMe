from backend.deployme.api.abc_scraper import *


class NFJScraper(ABCScraper):
    def __init__(self):
        super().__init__()
        self.__url = ("https://nofluffjobs.com/api/joboffers/main?pageTo=1&pageSize=20&withSalaryMatch=true"
                            "&salaryCurrency=PLN&salaryPeriod=month&region=pl&language=pl-PL")

    def scrape(self):
        try:
            response = requests.get(self.__url, headers=self._headers)
            if response.status_code == 200:
                data = response.json()

                for offer in data['postings']:
                    offer_data = {
                        'url': "https://nofluffjobs.com/pl/job/" + offer['url'],
                        'title': offer['title'],
                        'seniority': offer['seniority'],
                        'company': offer['name'],
                        'location': offer['location']['places'][0]['city'], # City
                        'salary_from': offer["salary"]["from"],
                        'salary_to': offer["salary"]["to"],
                        'currency': offer["salary"]["currency"],
                        'tiles': [tile["value"] for tile in offer["tiles"]["values"]]
                    }

                    if offer_data['seniority'] == 'Junior':
                        self._junior_offers.append(offer_data)

                    elif offer_data['seniority'] == 'Trainee':
                        self._trainee_offers.append(offer_data)
            else:
                print(f"Error: {response.status_code}")

        except Exception as e:
            print(f"Error: Failed to send request. {e}")


