from nfj_scraper import NFJScraper

scraper = NFJScraper()
trainee_offers = scraper.scrape("trainee", scrape_iterations=1)
# # print(f"Found {len(trainee_offers)} offers")
for offer in trainee_offers:
    print(f"{offer['url']} - {offer['company']} - {offer['title']} - {offer['salary']} - {offer['location']} - {offer['technologies']}")
# print()
# scraper2 = NFJScraper()
# junior_offers = scraper2.scrape("junior", scrape_iterations=1)
# print(f"Found {len(junior_offers)} offers")
# for offer in junior_offers:
#     print(f"{offer['url']} - {offer['company']} - {offer['title']} - {offer['salary']} - {offer['location']} - {offer['technologies']}")
# #
from sj_scraper import SJScraper

scraper3 = SJScraper()
offers = scraper3.scrape("junior", scrape_iterations=1)