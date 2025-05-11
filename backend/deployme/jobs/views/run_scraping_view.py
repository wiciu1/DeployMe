from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from ..services import run_scraping_and_save_to_db

class RunScrapingView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        try:
            # saves to DB
            offers = run_scraping_and_save_to_db()
            return Response ({
                'status': 'success',
                'offers_saved': len(offers)
            })
        except Exception as e:
            return Response ({
                'status': 'error',
                'message': str(e)
            }, status=500)

