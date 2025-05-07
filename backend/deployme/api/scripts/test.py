from scraper_manager import ScraperManager

scraper = ScraperManager()
offers = scraper.scrape_all(seniority="trainee", scrape_iterations=1)
for offer in offers:
    print(f"{offer['url']} - {offer['company']} - {offer['title']} - {offer['salary']} - {offer['location']} - {offer['technologies']}")