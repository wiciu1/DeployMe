from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from ..services import run_scraping_and_save_to_db

class RunScrapingView(APIView):
    permission_classes = [AllowAny,]

    def get(self, request, scrape_iterations):
        try:
            # saves to DB
            offers = run_scraping_and_save_to_db(scrape_iterations=scrape_iterations)
            return Response ({
                'status': 'success',
                'offers_saved': len(offers)
            })
        except Exception as e:
            return Response ({
                'status': 'error',
                'message': str(e)
            }, status=500)

