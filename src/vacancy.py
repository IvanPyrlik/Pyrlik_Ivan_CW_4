from typing import Tuple, Any


class Vacancy:
    """
    Класс для создания вакансий из данных.
    """

    def __init__(self,
                 vacancy_name: str,
                 url: str,
                 salary: int,
                 currency: str,
                 date_published: str,
                 description: str,
                 platform=None):
        self.__vacancy_name = vacancy_name
        self.__url = url
        self.__salary = salary
        self.__currency = currency
        self.__date_published = date_published
        self.__description = description
        self.platform_name = platform

    def __repr__(self):
        if self.__salary is None:
            return (f"На сайте {self.platform_name}.\n Вакансия - {self.__vacancy_name},\n "
                    f"зарплата не указана, ссылка - {self.__url}\n"
                    f"Дата публикации {self.__date_published}")
        elif self.__url is None:
            return (f"Вакансия - {self.__vacancy_name}, зарплата - {self.__salary}, cсылка - не указана.\n"
                    f"Дата публикации {self.__date_published}")
        return (f"Вакансия - {self.__vacancy_name}, зарплата - {self.__salary}, cсылка - {self.__url}\n"
                f"Дата публикации {self.__date_published}")

    def __gt__(self, other):
        """
        Метод сравнивает даты публикации.
        """
        return self.__date_published > other.date_published

    def __lt__(self, other):
        """
        Метод сравнивает даты публикации.
        """
        return self.__date_published < other.date_published

    def to_dict(self):
        """
        Метод для возвращения словаря в нужном виде.
        :return: Словарь в нужном виде
        """
        return {"vacancy_name": self.__vacancy_name,
                "url": self.__url,
                "salary": self.__salary,
                "currency": self.__currency,
                "date_published": self.__date_published,
                "description": self.__description}


class HeadHunterVacancy(Vacancy):
    """
    Подкласс для создания вакансий из данных HeadHunter.
    """
    platform_name = "HeadHunter"

    def __repr__(self):
        if self.__salary is None:
            return (f"На сайте {self.platform_name}.\n Вакансия - {self.__vacancy_name},\n зарплата не указана, ссылка - {self.__url}\n"
                    f"Дата публикации {self.__date_published}")
        return (f"На сайте {self.platform_name}.\n Вакансия - {self.__vacancy_name}, зарплата - {self.__salary}, cсылка - {self.__url}\n"
                f"Дата публикации {self.__date_published}")

    def to_dict(self):
        """
        Метод для возвращения словаря в нужном виде, с добалением платформы.
        :return: Словарь в нужном виде, с добалением платформы.
        """
        vacancy_dict = super().to_dict()
        vacancy_dict["platform"] = self.platform_name
        return vacancy_dict


class SuperJobVacancy(Vacancy):
    """
    Подкласс для создания вакансий из данных SuperJob.
    """
    platform_name = "SuperJob"

    def __repr__(self):
        if self.__salary is None:
            return (f"На сайте {self.platform_name}.\n Вакансия - {self.__vacancy_name},\n зарплата не указана, ссылка - {self.__url}\n"
                    f"Дата публикации {self.__date_published}")
        return (f"На сайте {self.platform_name}.\n Вакансия - {self.__vacancy_name}, зарплата - {self.__salary}, cсылка - {self.__url}\n"
                f"Дата публикации {self.__date_published}")

    def to_dict(self):
        """
        Метод для возвращения словаря в нужном виде, с добалением платформы.
        :return: Словарь в нужном виде, с добалением платформы.
        """
        vacancy_dict = super().to_dict()
        vacancy_dict["platform"] = self.platform_name
        return vacancy_dict
