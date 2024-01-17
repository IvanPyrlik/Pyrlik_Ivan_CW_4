import json
from abc import ABC, abstractmethod

from config import VACANCIES_PATH
from src.vacancy import Vacancy


class Saver(ABC):
    """
    Абстрактный класс для добавления вакансий,
    получения данных из файла по указанным критериям и
    удаления информации о вакансиях.
    """

    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def add_vacancies(self, vacancies: list[Vacancy]) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_vacancies(self, queries=None) -> list[dict]:
        raise NotImplementedError

    @abstractmethod
    def delete_vacancies(self, queries=None) -> None:
        raise NotImplementedError


class JsonSaver(Saver, ABC):
    """
    Класс для сохранения информации о вакансиях в JSON-файл.
    """
    def add_vacancies(self, vacancy: list[dict]) -> None:
        """
        Метод для добавления вакансий в файл.
        :param vacancy: Вакансии.
        :return: JSON-файл.
        """
        try:
            with open(VACANCIES_PATH, encoding='UTF-8') as file:
                data = json.load(file)
        except json.decoder.JSONDecodeError:
            data = []

        data.append(vacancy)

        with open(VACANCIES_PATH, "w", encoding='UTF-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def get_vacancies(self, query=None) -> list[dict]:
        """
        Метод для получения данных из файла по указанным критериям.
        :param query: Критерии.
        :return: Данные по указанным критериям.
        """
        with open(VACANCIES_PATH, encoding="utf-8") as file:
            all_vacancies = json.load(file)

        vacancies = []
        for vacancy in all_vacancies:
            if query == vacancy:
                vacancies.append(query)
        return vacancies

    def delete_vacancy(self, vacancy) -> None:
        """
        Метод для удаления информации о вакансиях.
        :param vacancy: Критерии для удаления.
        :return: JSON-файл.
        """
        with open(VACANCIES_PATH, encoding="UTF-8") as file:
            vacancies = json.load(file)

        undel_vacancies = [obj for obj in vacancies if obj["url"] != vars(vacancy)["url"]]

        with open(VACANCIES_PATH, "w") as file:
            json.dump(undel_vacancies, file, indent=2, ensure_ascii=False)
