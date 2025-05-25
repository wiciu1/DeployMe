import django_filters
from django_filters import rest_framework as filters
from .models import JobOffer


class JobOfferFilter(django_filters.FilterSet):
    salary = filters.NumberFilter(field_name='salary', lookup_expr='lte')
    seniority = filters.CharFilter(field_name='seniority', lookup_expr='iexact')
    location = filters.CharFilter(field_name='location', lookup_expr='icontains')
    technologies = filters.CharFilter(
        field_name='technologies',
        lookup_expr='icontains'
    )

    class Meta:
        model = JobOffer
        fields = ['salary', 'seniority', 'location', 'technologies']