import requests
from abstract import API
from vacancy import Vacancy
from data_error import DataError


class SuperJob(API):
    def __init__(self, keyword):
        self.__params = {
            'keywords': keyword,
            'sort_new (unixtime)': 1,
            'page': 0,
            'count': 10
        }

    def get_requests(self):
        """ Выполняет запрос по заданным параметрам """

        url = "https://api.superjob.ru/2.0/vacancies/"
        headers = {'X-Api-App-Id': 'v3.r.137674552.b6a9d0979a68caf85738e74388622082e27eda22.fdbe2c04b60f10d39a60651a38c21a3dc66ec9f4'}

        response = requests.get(url, params=self.__params, headers=headers)
        if response.status_code != 200:
            raise DataError
        return response.json()['objects']

    def parsing(self, data_list):
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

    def get_vacancies(self):
        """ Получает список вакансий"""

        try:
            vac_list = self.get_requests()
        except DataError:
            pass
        else:
            return self.parsing(vac_list)


super_job_api = SuperJob('Python')
super_vacancies = super_job_api.get_vacancies()
print(super_vacancies)
