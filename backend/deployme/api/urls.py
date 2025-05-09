from django.urls import path
from .views.job_offer_view import JobOfferListView

urlpatterns = [
    path('job-offers/', JobOfferListView.as_view(), name="job-offer-list"),
]