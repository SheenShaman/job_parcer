from head_hunter import HeadHunter
from super_job import SuperJob
from save_to_json import JSONSaver
from utils import sort_top


def main():
    # Получение поискового запроса
    greeting = input('Привет!\nВведите, что вы хотите найти: ')

    # Создание экземпляров для работы с API
    hh_api = HeadHunter(greeting)
    super_job_api = SuperJob(greeting)

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

    source = input('С какой платформы вы хотите получить вакансии(Введите "HH", "SJ" или "all")?\n')
    vacancies = all_vacancies
    if source.lower() == 'hh':
        vacancies = hh_vac
    elif source.lower() == 'sj':
        vacancies = sj_vac
    elif source.lower() == 'all':
        vacancies = all_vacancies
    else:
        print('Нет такого источника, по умолчанию значение "all"')

    while True:
        command = input('Если вы хотите вывести топ вакансий по зарплате введите команду "top"\n'
                        'Если вы хотите завершить программу введите команду "stop"\n')

        if command == 'top':
            top_n = int(input('\nВведите сколько вакансий вы хотите: '))
            sorted_vacancy = sort_top(vacancies, top_n)
            for vac in sorted_vacancy:
                print(vac)
        elif command == 'stop':
            print('Всего доброго!')
            break

        action = input('\nЕсли вы хотите вытянуть определенную вакансию, введите каманду "pull"\n'
                       'Если вы хотите удалить определенную вакансию, введите каманду "del"\n'
                       'Если вы хотите завершить программу введите команду "stop"\n')

        if action == 'pull':
            pull_id = input('Введите id вакансии, которую хотите вывести:\n')
            print(json_saver.pulling(pull_id))
        elif action == 'del':
            del_id = input('Введите id вакансии, которую хотите удалить:\n')
            json_saver.deleting(del_id)
        elif action == 'stop':
            print('Всего доброго!')
            break
        else:
            print("Такой команды нет")
            continue


if __name__ == '__main__':
    main()
