from datetime import datetime
from src.vacancy import Vacancy


def filter_vacancies(hh_vacancies: list[dict], sj_vacancies: list[dict], filter_words) -> list[Vacancy]:
    """
    Функция для фильтрации вакансий по ключевым словам.
    """
    vacancies = []
    if hh_vacancies is not None:
        for vacancy in hh_vacancies:
            for word in filter_words:
                if word.lower() in vacancy["name"].lower():
                    vacancies.append(Vacancy(vacancy_name=vacancy["name"],
                                             url=vacancy["alternate_url"],
                                             salary=vacancy["salary"],
                                             date_published=get_formatted_date_hh(vacancy['published_at']),
                                             description=vacancy["snippet"]["responsibility"]))

    if sj_vacancies is not None:
        for vacancy in sj_vacancies:
            for word in filter_words:
                if word.lower() in vacancy["profession"]:
                    vacancies.append(Vacancy(vacancy_name=vacancy["profession"],
                                             url=vacancy["link"],
                                             salary=vacancy["payment_from"],
                                             date_published=get_formatted_date_sj(vacancy[str("date_published")]),
                                             description=vacancy["work"]))
    return vacancies


def sort_vacancies(filtered_vacancies):
    """
    Функция для сортировки списка вакансий по зарплате.
    """
    return sorted(filtered_vacancies, key=lambda v: v.salary or 0, reverse=True)


def get_top_vacancies(filtered_vacancies, top_n):
    """
    Получение первых top_n вакансий.
    """
    return filtered_vacancies[:top_n]


def print_vacancies(vacancies):
    """
    Вывод всех вакансий.
    """
    count = 0
    for vacancy in vacancies:
        count += 1
        print(f'{count}.{vacancy}')


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
