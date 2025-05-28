import django_filters
from django_filters import rest_framework as filters
from django.db.models import Q
from .models import JobOffer, Technology


class JobOfferFilter(django_filters.FilterSet):
    # salary = filters.NumberFilter(field_name='salary', lookup_expr='lte')
    seniority = filters.CharFilter(method='filter_seniority')
    location = filters.CharFilter(field_name='location', lookup_expr='icontains')
    portal = filters.CharFilter(field_name='portal', lookup_expr='iexact')
    technologies = django_filters.CharFilter(method='filter_technologies')

    class Meta:
        model = JobOffer
        fields = ['seniority', 'location', 'portal', 'technologies']

    def filter_technologies(self, queryset, name, value):
        values = value.split(',')
        q_object = Q()
        for val in values:
            q_object |= Q(technologies__name__iexact=val.strip())
        return queryset.filter(q_object)

    def filter_seniority(self, queryset, name, value):
        values = value.split(',')
        q_object = Q()
        for val in values:
            q_object |= Q(seniority__iexact=val.strip())
        return queryset.filter(q_object)

