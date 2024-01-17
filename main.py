from config import VACANCIES_PATH
from src.api import HeadHunterAPI, SuperJobAPI
from src.engine import JsonSaver
from src.utils import print_vacancies, filter_vacancies, sort_vacancies, get_top_vacancies


def main():
    """
    Главная функция проекта.
    """
    hh_api = HeadHunterAPI()
    sj_api = SuperJobAPI()
    print("Здравствуйте!")
    top_n = int(input("Введите количество вакансий для вывода: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    hh_vacancies = hh_api.get_vacancies(filter_words)
    sj_vacancies = sj_api.get_vacancies(filter_words)
    filtered_vacancies = filter_vacancies(hh_vacancies, sj_vacancies, filter_words)
    json_saver = JsonSaver

    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    sorted_vacancies = sort_vacancies(filtered_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)
    json_saver.add_vacancies(hh_vacancies, sj_vacancies)


if __name__ == '__main__':
    main()
