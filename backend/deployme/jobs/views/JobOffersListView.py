from django.http import JsonResponse

from ..filters import JobOfferFilter
from ..models import JobOffer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from ..serializers.job_offer_serializer import JobOfferSerializer
from django_filters.rest_framework import DjangoFilterBackend

class JobOffersListView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = JobOffer.objects.all()
    serializer_class = JobOfferSerializer
    filterset_class = JobOfferFilter
    filter_backends = [DjangoFilterBackend]