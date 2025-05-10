from django.views import View
from django.http import JsonResponse
from jobs.models import JobOffer
from rest_framework.permissions import AllowAny
from ..services import run_scraping_and_save_to_db


# Activate scraping script
class RunScrapingView(View):
    def get(self, request, *args, **kwargs):
        try:
            # saves to DB
            offers = run_scraping_and_save_to_db()
            return JsonResponse({'status': 'success', 'offers_saved': len(offers)})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

