import os
import json
from abstract import JSON


class FileMixin:

    @staticmethod
    def make_dir(filename):
        """  """
        if not os.path.exists(os.path.dirname(filename)):
            os.mkdir(os.path.dirname(filename))

        if not os.path.exists(filename):
            with open(filename, 'w') as file:
                file.write(json.dumps([]))

    @staticmethod
    def open_file(filename):

        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)


class JSONSaver(FileMixin, JSON):
    def __init__(self, file_path):
        self.__file_path = file_path

    @property
    def file_path(self):
        return self.__file_path

    @file_path.setter
    def file_path(self, value):
        self.__file_path = value
        self.writing_data(self.__file_path)

    def writing_data(self, data):
        """ Записывает данные в файл """

        file_data = self.open_file(self.file_path)
        file_data.append(data)
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(file_data, file, indent=4, ensure_ascii=False)

    def pulling(self, id):
        """ Вытягивает данные по определенному запросу """

        file_data = self.open_file(self.file_path)

        result = []
        for item in file_data:
            if id == item['id']:
                result.append(item)

        return result

    def deleting(self, id):
        """ Удаляет данные по запросу """

        file_data = self.open_file(self.file_path)
        result = []
        for item in file_data:
            if id != item['id']:
                result.append(item)

        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(result, file, indent=4, ensure_ascii=False)

    def clear_data(self):
        """ Очищает файл от данных """

        with open(self.file_path, 'w') as file:
            file.write(json.dumps([]))
