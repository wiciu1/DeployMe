from django.http import JsonResponse
from jobs.models import JobOffer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from ..serializers.job_offer_serializer import JobOfferSerializer


class JobOffersListView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        offers = JobOffer.objects.all().order_by('url')

        serializer = JobOfferSerializer(offers, many=True)
        response = JsonResponse(serializer.data, safe=False)
        # For Polish Signs
        response['Content-Type'] = 'application/json; charset=utf-8'
        return response