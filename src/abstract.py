from abc import ABC, abstractmethod


class API(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_requests(self):
        """ Выполняет запрос по заданным параметрам """
        pass

    @abstractmethod
    def parsing(self, data_list):
        """ Разбивает данные на части """
        pass

    @abstractmethod
    def get_vacancies(self):
        """ Получает список вакансий"""
        pass


class JSON(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def writing_data(self, data):
        """ Записывает данные в файл """
        pass

    @abstractmethod
    def pulling(self, id):
        """ Вытягивает данные по определенному запросу """
        pass

    @abstractmethod
    def deleting(self, id):
        """ Удаляет данные по запросу """
        pass

    @abstractmethod
    def clear_data(self):
        """ Очищает файл от данных """
        pass
