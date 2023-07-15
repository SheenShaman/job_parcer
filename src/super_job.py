import requests
from abstract import API


class SuperJob(API):
    def __init__(self, keyword):
        self.__params = {
            'keywords': keyword,
            'sort_new (unixtime)': 1,
            'page': 0,
            'count': 10
        }


    def get_vacancies(self):

        url = "https://api.superjob.ru/2.0/vacancies/"
        headers = {'X-Api-App-Id': 'v3.r.137674552.b6a9d0979a68caf85738e74388622082e27eda22.fdbe2c04b60f10d39a60651a38c21a3dc66ec9f4'}

        response = requests.get(url, params=self.__params, headers=headers).json()
        return response


super_job_api = SuperJob('Python')
super_vacancies = super_job_api.get_vacancies()
print(super_vacancies)
