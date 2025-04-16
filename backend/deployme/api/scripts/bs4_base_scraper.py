from abc import abstractmethod, ABC
from bs4 import BeautifulSoup
import requests

class BS4BaseScraper(ABC):
    def __init__(self, headers=None):
        self.session = requests.Session()
        self.headers = headers or  {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
        }

    def get_soup(self, url):
        try:
            response = self.session.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            print(response.text[:5000])
            return BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            print(f'[Error] Failed to fetch {url}')
            return None

    @abstractmethod
    def scrape(self, seniority='junior', max_pages=10):
        pass
