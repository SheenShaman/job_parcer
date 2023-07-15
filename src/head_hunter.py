import requests
from abstract import API


class HeadHunterAPI(API):
    def __init__(self, keyword):
        self.__params = {
            'text': keyword,
            'page': 0,
            'per_page': 10
        }

    def get_vacancies(self):
        url = "https://api.hh.ru/vacancies"
        response = requests.get(url, params=self.__params).json()
        return response


hh_api = HeadHunterAPI('Python')
hh_vacancies = hh_api.get_vacancies()
print(hh_vacancies)
