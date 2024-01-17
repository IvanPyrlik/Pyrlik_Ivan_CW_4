import os
from abc import ABC, abstractmethod

import requests
from dotenv import load_dotenv

from config import HH_URL, SJ_URL

load_dotenv()


class API(ABC):
    """Абстрактный класс для работы с API сайтов с вакансиями."""
    @abstractmethod
    def get_vacancies(self, name) -> list[dict]:
        raise NotImplementedError


class HeadHunterAPI(API):
    """Подкласс для работы с API сайта HeadHunter."""

    def get_vacancies(self, name):
        """
        Метод для поиска на HeadHunter.
        :param name: Параметр поиска.
        :return: Выводит данные.
        """
        params = {"name": name, "page": 0, "per_page": 100}

        return requests.get(url=HH_URL, params=params).json().get("items")


class SuperJobAPI(API):
    """Подкласс для работы с API сайта SuperJob."""
    def get_vacancies(self, name):
        """
        Метод для поиска на SuperJob.
        :param name: Параметр поиска.
        :return: Выводит данные.
        """
        params = {"keyword": name, "page": 0, "count": 100}
        headers = {"X-Api-App-Id": os.getenv('SJ_API_KEY')}
        return requests.get(url=SJ_URL, params=params, headers=headers).json().get("objects")
