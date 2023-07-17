class Vacancy:
    def __init__(self, id, title, url, salary_from, salary_to, currency, employer, platform) -> None:
        """
        Класс для работы с вакансиями
        """
        self.id = id
        self.title = title
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.employer = employer
        self.platform = platform

    @property
    def salary(self) -> int:
        """ Считает среднюю зарплату """

        if self.salary_from > 0 and self.salary_to > 0:
            salary = int((self.salary_from + self.salary_to) / 2)
        elif self.salary_from > 0 and self.salary_to == 0:
            salary = self.salary_from
        else:
            salary = self.salary_to
        return salary

    def __gt__(self, other) -> bool:
        """ Сравнивает вакансии по зарплате """

        return self.salary > other.salary

    def __lt__(self, other) -> bool:
        """ Сравнивает вакансии по зарплате """

        return self.salary < other.salary

    def __repr__(self):
        """ Выводит информацию в режиме отладки """

        return f'{self.__class__.__name__}({self.title}, {self.url}, {self.salary},' \
               f' {self.currency}, {self.employer}, {self.platform})'

    def __str__(self):
        """ Выводит информацию для пользователя """

        return f'id ({self.id})\n{self.title} -> {self.url}\n{self.salary} {self.currency}\n' \
               f'{self.employer}\n{self.platform}\n'
