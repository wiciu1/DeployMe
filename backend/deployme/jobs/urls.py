from django.urls import path
from .views.JobOffersListView import JobOffersListView
from .views.run_scraping_view import RunScrapingView

urlpatterns = [
    path('job-offers-script/', RunScrapingView.as_view(), name="job-offer-scrape-list"),
    path('get-job-offers/', JobOffersListView.as_view(), name="job-offers-list"),
]