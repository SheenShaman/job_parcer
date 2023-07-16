
class Vacancy:
    def __init__(self, id, title, url, salary_from, salary_to, currency, employer, platform):
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
        salary = int((self.salary_from + self.salary_to) / 2)
        return salary

    def __gt__(self, other) -> bool:
        return self.salary > other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __repr__(self):
        return f'{self.__class__.__name__}({self.title}, {self.url}, {self.salary},' \
               f' {self.currency}, {self.employer}, {self.platform})'
