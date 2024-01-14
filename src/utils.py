import json
from datetime import datetime
from operator import itemgetter
from typing import List

from src.vacancy import HeadHunterVacancy, SuperJobVacancy, Vacancy


def create_hh_instances(vacancies: list[dict]) -> list[Vacancy]:
    """
    Метод для создания экземпляров класса для HeadHunter.
    :param vacancies: Нашедшиеся вакансии.
    :return: Список с экземлярами класса.
    """
    return [HeadHunterVacancy(vacancy_name=vacancy["name"],
                              url=vacancy["alternate_url"],
                              salary=vacancy["salary"],
                              currency=vacancy["salary"],
                              date_published=get_formatted_date_hh(vacancy["published_at"]),
                              description=vacancy["snippet"]["responsibility"])
            for vacancy in vacancies]


def create_sj_instances(vacancies: list[dict]) -> list[Vacancy]:
    """
    Метод для создания экземпляров класса для SuperJob.
    :param vacancies: Нашедшиеся вакансии.
    :return: Список с экземлярами класса.
    """
    return [SuperJobVacancy(vacancy_name=vacancy["profession"],
                            url=vacancy["link"],
                            salary=vacancy["payment_from"],
                            currency=vacancy["currency"],
                            date_published=get_formatted_date_sj(vacancy[str("date_published")]),
                            description=vacancy["work"])
            for vacancy in vacancies]


def get_formatted_date_hh(date: str) -> str:
    """
    Возвращает отформатированную дату для HeadHunter.
    """
    date_format_hh = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S+%f").strftime("%d.%m.%Y %X")
    return date_format_hh


def get_formatted_date_sj(date: int) -> str:
    """
    Возвращает отформатированную дату для SuperJob.
    """
    date_format_sj = datetime.fromtimestamp(int(date)).strftime("%d.%m.%Y %X")
    return date_format_sj


def get_top_vacancies_by_date(vacancies: list[Vacancy]) -> list[Vacancy]:
    """
    Функция сортирует вакансии по дате публикации.
    """
    sorted_list = sorted(vacancies, key=itemgetter("date_published"))
    return sorted_list


def convert_to_instance(vacancies: list[dict]) -> list[dict]:
    convert = []
    for vacancy in vacancies:
        convert.append(vacancy)
    return convert


def print_vacancies(vacancies):
    vacancy_dict = convert_to_instance(vacancies)
    print(str(vacancy_dict))
