import logging
from datetime import timezone, timedelta

from .jobscraper.scraping_manager import ScrapingManager
from .jobscraper.scraping_env import ScrapingEnv
from .models import JobOffer

logger = logging.getLogger(__name__)


def run_scraping_and_save_to_db(seniority, scrape_iterations=1):
    """
    Run scraping process and save results to database.

    Args:
        seniority (str): 'junior' or 'trainee'
        scrape_iterations (int): Number of times to load more offers

    Returns:
        dict: Results with status and statistics
    """
    env = None
    try:
        env = ScrapingEnv(headless=False)  # Run in headless mode for production
        manager = ScrapingManager(env)

        # Run scraping process
        stats = manager.scrape_all(seniority=seniority, scrape_iterations=scrape_iterations)

        logger.info(f"Scraping completed for {seniority} positions")

        return {
            'status': 'success',
            'stats': dict(stats),
            'seniority': seniority,
            'iterations': scrape_iterations
        }

    except Exception as e:
        logger.error(f"Scraping failed: {str(e)}", exc_info=True)
        return {
            'status': 'error',
            'error': str(e),
            'seniority': seniority
        }

    finally:
        if env:
            env.quit()


def cleanup_old_offers(days=30):
    try:
        cutoff_date = timezone.now() - timedelta(days=days)

        old_offers = JobOffer.objects.filter(created_at__lt=cutoff_date)

        deleted, _ = old_offers.delete()
        logger.info(f"Deleted {deleted} job offers older than {days} days.")
        return
    except Exception as e:
        logger.error(f'Failed to delete old offers: {str(e)}', exc_info=True)
