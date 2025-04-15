from nfj_scraper import NFJScraper

scraper = NFJScraper()
offers = scraper.scrape(scrape_intervals=2)
print(f"Found {len(offers)} offers")
for offer in offers:
    print(f"{offer['url']} - {offer['company']} - {offer['title']} - {offer['salary']} - {offer['location']} - {offer['technologies']}")