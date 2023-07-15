
from abc import ABC, abstractmethod


class API(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        """ Получает список вакансий"""
        pass
