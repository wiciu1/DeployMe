from django.http import JsonResponse
from django.views import View
from jobs.models import JobOffer
from ..serializers.job_offer_serializer import JobOfferSerializer

class JobOffersListView(View):
    def get(self, request, *args, **kwargs):
        offers = JobOffer.objects.all().order_by('url')[:10]

        serializer = JobOfferSerializer(offers, many=True)
        response = JsonResponse(serializer.data, safe=False)
        # For Polish Signs
        response['Content-Type'] = 'application/json; charset=utf-8'
        return response