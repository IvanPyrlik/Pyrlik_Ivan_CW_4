class Vacancy:
    """Класс для создания вакансий из данных"""
    def __init__(self, vacancy_name: str, url: str, salary_from: int, salary_to: int, currency: str, description: str):
        self.__vacancy_name = vacancy_name
        self.__url = url
        self.__salary_from = self.transformation_salary(salary_from)
        self.__salary_to = self.transformation_salary(salary_to)
        self.__currency = currency
        self.__description = description

    def __str__(self):
        return (f'Название вакансии: {self.__vacancy_name}, '
                f'зарплата: от {self.__salary_from} до {self.__salary_to} {self.__currency}, '
                f'ссылка на вакансию: {self.__url}.')

    @staticmethod
    def transformation_salary(salary) -> int:
        """
        Метод для зарплаты.
        :param salary: Зарплата.
        :return: Если зарплата None, выводит 0.
        """
        if salary is None:
            return 0
        return salary

    def __gt__(self, other) -> int:
        """Метод сравнения - больше."""
        return int(self.__salary_from) > int(other.salary_from)

    def __lt__(self, other) -> int:
        """Метод сравнения - меньше."""
        return int(other.salary_to) < int(self.__salary_to)

    def __eq__(self, other) -> int:
        """Метод сравнения - равенство."""
        return int(self.__salary_from) == int(other.salary_from)


class HeadHunterVacancy(Vacancy):
    """Подкласс для создания вакансий из данных HeadHunter"""

    def __str__(self):
        return (f'На HeadHunter для вас нашлось - название вакансии: {self.__vacancy_name}, '
                f'зарплата: от {self.__salary_from} до {self.__salary_to} {self.__currency}, '
                f'ссылка на вакансию: {self.__url}.')


class SuperJobVacancy(Vacancy):
    """Подкласс для создания вакансий из данных SuperJob"""

    def __str__(self):
        return (f'На SuperJob для вас нашлось - название вакансии: {self.__vacancy_name}, '
                f'зарплата: от {self.__salary_from} до {self.__salary_to} {self.__currency}, '
                f'ссылка на вакансию: {self.__url}.')








