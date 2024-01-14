import os
from abc import ABC, abstractmethod

import requests
from dotenv import load_dotenv

from config import HH_URL, SJ_URL

load_dotenv()


class API(ABC):
    """Абстрактный класс для работы с API сайтов с вакансиями."""
    @abstractmethod
    def get_vacancies(self) -> list[dict]:
        raise NotImplementedError


class HeadHunterAPI(API):
    """Подкласс для работы с API сайта HeadHunter."""
    def __init__(self, query: str, amount_vacancies: int):
        self.query = query
        self.amount_vacancies = amount_vacancies
        self.params = {"text": self.query, "per_page": self.amount_vacancies}

    def get_vacancies(self, page=0) -> list[dict]:
        """
        Метод для поиска на HeadHunter.
        :param page: Номер страницы начала поиска.
        :return: Выводит данные.
        """
        self.params["page"] = page
        return requests.get(url=HH_URL, params=self.params).json()["items"]


class SuperJobAPI(API):
    """Подкласс для работы с API сайта SuperJob."""
    def __init__(self, query: str, amount_vacancies: int):
        self.query = query
        self.amount_vacancies = amount_vacancies
        self.params = {"keyword": self.query, "count": self.amount_vacancies}

    def get_vacancies(self, page=0) -> list[dict]:
        """
        Метод для поиска на SuperJob.
        :param page: Номер страницы начала поиска.
        :return: Выводит данные.
        """
        self.params["page"] = page
        headers = {"X-Api-App-Id": os.getenv('SJ_API_KEY')}
        return requests.get(url=SJ_URL, params=self.params, headers=headers).json().get("objects")
