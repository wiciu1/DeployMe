from abc import ABC, abstractmethod
import requests

class ABCScraper(ABC):
    def __init__(self):
        self._all_offers = []
        self._trainee_offers = []
        self._junior_offers = []
        self._headers = {
            "Accept": "application/json",
            "Accept-Language": "pl-PL",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        }

    @abstractmethod
    def scrape(self):
        pass
