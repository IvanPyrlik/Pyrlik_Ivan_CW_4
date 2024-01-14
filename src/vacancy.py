class Vacancy:
    """
    Класс для создания вакансий из данных.
    """

    def __init__(self, vacancy_name: str, url: str, salary: int, currency: str, date_published: str, description: str):
        self.__vacancy_name = vacancy_name
        self.__url = url
        self.__salary = salary
        self.__currency = currency
        self.__date_published = date_published
        self.__description = description

    def __str__(self):
        return (f'Название вакансии: {self.__vacancy_name}, '
                f'зарплата: от {self.__salary.get('from')} '
                f'до {self.__salary.get('to')} {self.__salary.get('currency')}, '
                f'ссылка на вакансию: {self.__url}.')

    @property
    def get_salary(self) -> str:
        """
        Метод возвращает зарплату в отформатированном виде.
        """

        if self.__salary is not None:

            if self.__salary.get('from') not in [0, None] and self.__salary.get('to') not in [0, None]:
                return (f"По вакансии {self.__vacancy_name} зарплата "
                        f"от {self.__salary.get('from')} "
                        f"до {self.__salary.get('to')} {self.__salary.get('currency')}.")

            elif self.__salary.get('from') == 0 or None and self.__salary.get('to') == 0 or None:
                return f'По вакансии {self.__vacancy_name} зарплата не указана.'

            elif self.__salary.get('from') in [0, None] and self.__salary.get('to') not in [0, None]:
                return (f"По вакансии {self.__vacancy_name} зарплата "
                        f"до {self.__salary.get('to')} {self.__salary.get('currency')}.")

            elif self.__salary.get('from') not in [0, None] and self.__salary.get('to') in [0, None]:
                return (f"По вакансии {self.__vacancy_name} зарплата "
                        f"от {self.__salary.get('from')} {self.__salary.get('currency')}.")

        else:
            return f'По вакансии {self.__vacancy_name} зарплата не указана.'

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

    def __str__(self):
        return (f'На HeadHunter для вас нашлось - название вакансии: {self.__vacancy_name}, '
                f'зарплата: от {self.__salary.get('from')} '
                f'до {self.__salary.get('to')} {self.__salary.get('currency')}, '
                f'ссылка на вакансию: {self.__url}.')

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

    def __str__(self):
        return (f'На SuperJob для вас нашлось - название вакансии: {self.__vacancy_name}, '
                f'зарплата: от {self.__salary.get('from')} '
                f'до {self.__salary.get('to')} {self.__salary.get('currency')}, '
                f'ссылка на вакансию: {self.__url}.')

    def to_dict(self):
        """
        Метод для возвращения словаря в нужном виде, с добалением платформы.
        :return: Словарь в нужном виде, с добалением платформы.
        """
        vacancy_dict = super().to_dict()
        vacancy_dict["platform"] = self.platform_name
        return vacancy_dict
