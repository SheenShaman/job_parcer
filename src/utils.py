from vacancy import Vacancy


def sort_top(all_vacancies: list[Vacancy], num: int) -> list[Vacancy]:
    return sorted(all_vacancies, reverse=True)[:num]
