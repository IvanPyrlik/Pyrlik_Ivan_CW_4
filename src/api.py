import os
from abc import ABC, abstractmethod

import requests
from dotenv import load_dotenv

from config import HH_URL, SJ_URL

load_dotenv()


class API(ABC):
    """Абстрактный класс для поиска данных."""
    @abstractmethod
    def get_response(self) -> list[dict]:
        raise NotImplementedError


class HeadHunterAPI(API):
    """Подкласс для поиска на HeadHunter."""
    def __init__(self, query: str):
        self.query = query
        self.params = {"text": self.query, "per_page": 100, "search_field": "name"}

    def get_response(self, page=0) -> list[dict]:
        self.params["page"] = page
        return requests.get(url=HH_URL, params=self.params).json()["items"]


class SuperJobAPI(API):
    """Подкласс для поиска на SuperJob."""
    def __init__(self, query: str):
        self.query = query
        self.params = {"keyword": self.query, "count": 100}

    def get_response(self, page=0) -> list[dict]:
        self.params["page"] = page
        headers = {"X-Api-App-Id": os.getenv('SJ_API_KEY')}
        return requests.get(url=SJ_URL, params=self.params, headers=headers).json()["objects"]

