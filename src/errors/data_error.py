class DataError(Exception):
    def __init__(self, message="Ошибка данных", *args):
        super().__init__(message, *args)
