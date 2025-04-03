import os
from abc import ABC, abstractmethod
from dotenv import load_dotenv

load_dotenv()

class NASADataFetcher(ABC):
    def __init__(self):
        self.api_key = os.getenv("NASA_API_KEY")
        self.base_url = "https://api.nasa.gov"

    @abstractmethod
    def fetch_data(self):
        pass