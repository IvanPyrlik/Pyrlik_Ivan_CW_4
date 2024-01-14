from pathlib import Path

HH_URL = "https://api.hh.ru/vacancies"
SJ_URL = "https://api.superjob.ru/2.0/vacancies/"

FILE_PATH = Path(__file__).parent
VACANCIES_PATH = Path.joinpath(FILE_PATH, "data", "vacancies.json")
