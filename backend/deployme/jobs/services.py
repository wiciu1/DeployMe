from .jobscraper.scraping_manager import ScrapingManager
from .jobscraper.scraping_env import ScrapingEnv
from .models import JobOffer


# Scraping Script
def run_scraping_and_save_to_db():
    env = ScrapingEnv()
    manager = ScrapingManager(env)
    env.set_manager(manager=manager)
    manager.scrape_all()
    env.quit()


    for offer_data in manager.all_offers:
        try:
            JobOffer.objects.get_or_create(
                # URL as ID
                url = offer_data['url'],
                defaults = {
                    'title': offer_data['title'],
                    'seniority': offer_data['seniority'],
                    'company': offer_data['company'],
                    'location': offer_data['location'],
                    'salary': offer_data['salary'],
                    'technologies': offer_data['technologies'],
                }
            )
        except Exception as e:
            print(e)

    return manager.all_offers