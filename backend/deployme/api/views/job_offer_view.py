from django.views import View
from django.http import JsonResponse
from jobs.models import JobOffer
from rest_framework.permissions import AllowAny
from jobs.jobscraper.scraping_manager import ScrapingManager
from jobs.jobscraper.scraping_env import ScrapingEnv

class JobOfferListView(View):
    def get(self, request, *args, **kwargs):
        env = ScrapingEnv()
        manager = ScrapingManager(env)
        env.set_manager(manager=manager)
        manager.scrape_all()
        env.quit()

        return JsonResponse(manager.all_offers, safe=False)
