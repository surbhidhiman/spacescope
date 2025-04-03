import requests

from models import Session, APOD
from nasa.base import NASADataFetcher

class APODFetcher(NASADataFetcher):
    def __init__(self):
        super().__init__()
        self.endpoint = f"{self.base_url}/planetary/apod"

    def fetch_data(self, date=None):
        params = {
            "api_key": self.api_key,
        }
        if date:
            params["date"] = date

        response = requests.get(self.endpoint, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch APOD:", response.status_code)
            return None
        
    def save_to_db(self, response):
        session = Session()

        existing = session.query(APOD).filter_by(date=response["date"]).first()
        if not existing:
            record = APOD(
                date=response["date"],
                title=response["title"],
                explanation=response["explanation"],
                hdurl=response["hdurl"],
                url=response["url"]
            )
            session.add(record)
            print(f"Saved new APOD to the database.")

        session.commit()
        session.close()