import requests
from src.abstract import API
from src.platforms.vacancy import Vacancy
from src.errors.data_error import DataError


class HeadHunter(API):
    """
    Класс для работы с API HeadHunter
    """
    def __init__(self, keyword: str) -> None:
        self.__params = {
            'text': {keyword},
            'page': 0,
            'per_page': 50
        }

    def get_requests(self) -> list:
        """ Выполняет запрос по заданным параметрам """

        url = "https://api.hh.ru/vacancies/"
        response = requests.get(url, params=self.__params)
        if response.status_code != 200:
            raise DataError
        return response.json()['items']

    def parsing(self, data_list: list) -> list:
        """ Разбивает данные на части """

        vacancies = []
        for vac in data_list:
            salary_from, salary_to, currency = self.get_salary(vac['salary'])
            vacancy = Vacancy(vac['id'],
                              vac['name'],
                              vac['alternate_url'],
                              salary_from,
                              salary_to,
                              currency,
                              vac['employer']['name'],
                              'HeadHunter')
            vacancies.append(vacancy)
        return vacancies

    @staticmethod
    def get_salary(salary: dict) -> list:
        """ Преобразует параметр salary в нужный формат """

        new_salary = [0, 0, None]
        if salary and salary['from']:
            new_salary[0] = salary['from']
            new_salary[2] = salary['currency']
        if salary and salary['to']:
            new_salary[0] = salary['to']
        return new_salary

    def get_vacancies(self) -> list:
        """ Получает список вакансий"""

        try:
            vac_list = self.get_requests()
        except DataError:
            pass
        else:
            return self.parsing(vac_list)
