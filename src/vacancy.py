class Vacancy:
    """
    Класс для создания вакансий из данных.
    """

    def __init__(self,
                 vacancy_name: str,
                 url: str,
                 salary: int,
                 date_published: str,
                 description: str):
        self.vacancy_name = vacancy_name
        self.url = url
        self.salary = salary
        self.date_published = date_published
        self.description = description

    def __repr__(self):
        if self.salary is None:
            return (f"Вакансия - {self.vacancy_name},\n "
                    f"зарплата не указана, ссылка - {self.url}\n"
                    f"Дата публикации {self.date_published}")
        elif self.url is None:
            return (f"Вакансия - {self.vacancy_name}, зарплата - {self.salary}, cсылка - не указана.\n"
                    f"Дата публикации {self.date_published}")
        return (f"Вакансия - {self.vacancy_name}, зарплата - {self.salary}, cсылка - {self.url}\n"
                f"Дата публикации {self.date_published}")

    def __gt__(self, other):
        """
        Переопределение метода сравнения >.
        """
        return self.salary > other.salary

    def __lt__(self, other):
        """
        Сравнение зарплат вакансий.
        """
        return self.salary or 0 < other.salary or 0

    def __eq__(self, other):
        """
        Переопределение метода сравнения ==.
        """
        return self.salary == other.salary

    def __le__(self, other):
        """
        Переопределение метода сравнения <=.
        """
        return self.salary <= other.salary

    def __ge__(self, other):
        """
        Переопределение метода сравнения >=.
        """
        return self.salary >= other.salary


class HeadHunterVacancy(Vacancy):
    """
    Подкласс для создания вакансий из данных HeadHunter.
    """
    def __repr__(self):
        if self.salary is None:
            return (f"Вакансия - {self.vacancy_name},\n "
                    f"зарплата не указана, ссылка - {self.url}\n"
                    f"Дата публикации {self.date_published}")
        return (f"Вакансия - {self.vacancy_name}, "
                f"зарплата - {self.salary}, cсылка - {self.url}\n"
                f"Дата публикации {self.date_published}")


class SuperJobVacancy(Vacancy):
    """
    Подкласс для создания вакансий из данных SuperJob.
    """
    def __repr__(self):
        if self.salary is None:
            return (f"Вакансия - {self.vacancy_name},\n "
                    f"зарплата не указана, ссылка - {self.url}\n"
                    f"Дата публикации {self.date_published}")
        return (f"Вакансия - {self.vacancy_name}, "
                f"зарплата - {self.salary}, cсылка - {self.url}\n"
                f"Дата публикации {self.date_published}")
