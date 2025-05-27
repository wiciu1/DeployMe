from celery import shared_task
from datetime import timedelta
from django.utils import timezone
from .models import JobOffer
from .services import run_scraping_and_save_to_db, cleanup_old_offers
import logging

logger = logging.getLogger(__name__)

@shared_task(bind=True, max_retries=3)
def run_daily_scraping_task(self):
    try:
        result = run_scraping_and_save_to_db(seniority='junior', scrape_iterations=1)
        if result['status'] == 'error':
            raise Exception(result['error'])

        return result
    except Exception as e:
        logger.error(f"Scraping failed, retrying: {str(e)}")
        raise self.retry(exc=e, countdown=60 * 5)  # Retry after 5 minutes

@shared_task
def cleanup_old_offers_task():
    try:
        cleanup_old_offers(days=30)
    except Exception as e:
        logger.error(f"Cleanup failed: {str(e)}")
        raise Exception(e)