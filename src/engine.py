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


class JsonSaver(Saver):
    """
    Класс для сохранения информации о вакансиях в JSON-файл.
    """
    def add_vacancies(self, vacancies: list[Vacancy]) -> None:
        """
        Метод для добавления вакансий в файл.
        :param vacancies: Вакансии.
        :return: JSON-файл.
        """
        vacancies_json = [vacancy.to_dict() for vacancy in vacancies]
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(vacancies_json, file)

    def get_vacancies(self, query=None) -> list[dict]:
        """
        Метод для получения данных из файла по указанным критериям.
        :param query: Критерии.
        :return: Данные по указанным критериям.
        """
        with open(self.path, encoding="utf-8") as file:
            all_vacancies = json.load(file)

        vacancies = []
        for query in all_vacancies:
            vacancies.append(query)
        return vacancies

    def delete_vacancies(self, query=None) -> None:
        """
        Метод для удаления информации о вакансиях.
        :param query: Критерии для удаления.
        :return: JSON-файл.
        """
        with open(self.path, encoding="utf-8") as file:
            all_vacancies = json.load(file)

        vacancies = []
        for query in all_vacancies:
            vacancies.append(query)
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(vacancies, file)


def load_json() -> list[Vacancy]:
    with open(VACANCIES_PATH, encoding="utf-8") as json_file:
        vacancy_json = json.load(json_file)
    filter_vacancy = []
    for vacancy in vacancy_json:
        filter_vacancy.append(Vacancy(vacancy["vacancy_name"],
                                      vacancy["url"],
                                      vacancy["salary"],
                                      vacancy["salary"],
                                      vacancy["date_published"],
                                      vacancy["description"],
                                      vacancy["platform"]))
    return filter_vacancy
