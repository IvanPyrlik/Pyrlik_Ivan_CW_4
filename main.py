from config import VACANCIES_PATH
from src.api import HeadHunterAPI, SuperJobAPI
from src.engine import JsonSaver, load_json
from src.utils import create_hh_instances, create_sj_instances, get_top_vacancies_by_date, print_vacancies


def main():
    search_query = input("Введите поисковый запрос: ").lower()
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").lower().split()
    top_n = int(input("Введите количество вакансий для вывода в топ N c HeadHunter и SuperJob: "))

    hh_api = HeadHunterAPI(search_query, top_n)
    superjob_api = SuperJobAPI(search_query, top_n)

    hh_vacancies = hh_api.get_vacancies()
    superjob_vacancies = superjob_api.get_vacancies()

    hh_instances = create_hh_instances(hh_vacancies)
    sj_instances = create_sj_instances(superjob_vacancies)

    json_saver = JsonSaver(VACANCIES_PATH)
    json_saver.add_vacancies(hh_instances + sj_instances)
    json_saver.get_vacancies(filter_words)

    all_vacancy = load_json()
    print_vacancies(repr(all_vacancy))


if __name__ == '__main__':
    main()
