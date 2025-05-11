import django_filters
from .models import JobOffer

class JobOfferFilter(django_filters.FilterSet):
    class Meta:
        model = JobOffer
        fields = {

        }