from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.throttling import UserRateThrottle

from ..services import run_scraping_and_save_to_db


class ScrapingThrottle(UserRateThrottle):
    scope = 'scraping'  # Configure in Django settings


class RunScrapingView(APIView):
    permission_classes = [AllowAny]
    throttle_classes = [ScrapingThrottle]  # Prevent abuse

    def get(self, request, scrape_iterations):
        """
        API endpoint to trigger scraping process.

        Args:
            scrape_iterations (int): Number of times to load more offers

        Returns:
            Response: JSON response with scraping results
        """
        try:
            # Validate input
            try:
                scrape_iterations = int(scrape_iterations)
                if scrape_iterations < 1 or scrape_iterations > 10:  # Set reasonable limits
                    raise ValueError("Scrape iterations must be between 1 and 10")
            except ValueError as e:
                return Response({
                    'status': 'error',
                    'message': str(e)
                }, status=status.HTTP_400_BAD_REQUEST)

            # Run scraping process
            results = run_scraping_and_save_to_db(
                seniority='junior',
                scrape_iterations=scrape_iterations
            )

            # Handle response
            if results['status'] == 'error':
                return Response({
                    'status': 'error',
                    'message': results.get('error', 'Unknown error occurred'),
                    'seniority': results.get('seniority', 'unknown')
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response({
                'status': 'success',
                'data': results,
                'iterations': scrape_iterations
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'status': 'error',
                'message': f"Unexpected error: {str(e)}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)