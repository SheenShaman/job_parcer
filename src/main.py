from head_hunter import HeadHunter
from super_job import SuperJob
from save_to_json import JSONSaver


def main():
    # Создание экземпляров для работы с API
    hh_api = HeadHunter("Python")
    super_job_api = SuperJob("Python")

    # Получение вакансий с разных платформ
    hh_vac = hh_api.get_vacancies()
    sj_vac = super_job_api.get_vacancies()

    # Сохранение информации о вакансиях в файл
    json_saver = JSONSaver('vacancies/vacancies.json')
    json_saver.make_dir('vacancies/vacancies.json')
    json_saver.clear_data()

    all_vacancies = hh_vac + sj_vac

    for vac in all_vacancies:
        json_saver.writing_data(vac.__dict__)

    source = input('С какой платформы вы хотите получить вакансии(Введите "hh", "SJ" или "all")?\n')
    vacancies = all_vacancies
    if source.lower() == 'hh':
        vacancies = hh_vac
    elif source.lower() == 'SJ':
        vacancies = sj_vac
    elif source.lower() == 'all':
        vacancies = all_vacancies
    else:
        print('Нет такого источника, по умолчанию значение "all"')

    while True:
        pass

    #for vac in vacancies:
    #    print(vac)


if __name__ == '__main__':
    main()
