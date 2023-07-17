import os
import requests
from src.abstract import API
from src.platforms.vacancy import Vacancy
from src.errors.data_error import DataError


class SuperJob(API):
    """
    Класс для работы с API SuperJob
    """
    def __init__(self, keyword: str) -> None:
        self.__params = {
            'keywords': keyword,
            'sort_new (unixtime)': 1,
            'page': 0,
            'count': 50
        }

    def get_requests(self) -> list:
        """ Выполняет запрос по заданным параметрам """
        api_key: str = os.getenv('Super_Job_API_KEY')
        url = "https://api.superjob.ru/2.0/vacancies/"
        headers = {'X-Api-App-Id': api_key}

        response = requests.get(url, params=self.__params, headers=headers)
        if response.status_code != 200:
            raise DataError
        return response.json()['objects']

    def parsing(self, data_list: list) -> list:
        """ Разбивает данные на части """

        vacancies = []
        for vac in data_list:
            vacancy = Vacancy(vac['id'],
                              vac['profession'],
                              vac['link'],
                              vac['payment_from'],
                              vac['payment_to'],
                              vac['currency'],
                              vac['firm_name'],
                              'Superjob')
            vacancies.append(vacancy)
        return vacancies

    def get_vacancies(self) -> list:
        """ Получает список вакансий"""

        try:
            vac_list = self.get_requests()
        except DataError:
            pass
        else:
            return self.parsing(vac_list)
