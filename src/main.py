"""Основная работа программы"""

from src.filemanager import JSONFileManager
from src.vacancies import Vacancy
from src.vacanciesfilter import VacanciesFilter
from src.vacancyapimanager import HeadHunterAPIManager, SuperJobAPIManager


def print_services():
    """Функция запрос на работу с сайтом - HH, SJ или HH и SJ"""
    print("Выберите сервис, с которым хотите работать")
    print("1 - Head Hunter")
    print("2 - Super Job")
    print("3 - Head Hunter и Super Job")


def print_output_variants():
    """Функция, которая предоставляет запись в формат файла или вывести на консоль"""
    print("Что делать с результатами")
    print("1 - Вывести на экран")
    print("2 - Сохранить в json-файл")


def print_vacancies(vacancies: list[Vacancy]):
    for vac in vacancies:
        print(vac.salary, vac.title)


def user_interaction():
    hh = HeadHunterAPIManager()
    sj = SuperJobAPIManager()
    services = {"1": [hh], "2": [sj], "3": [hh, sj], }
    while True:
        print_services()
        user_input = input("Ваш выбор: ")
        managers = services.get(user_input)
        if managers:
            break
        print("\nТакого варианта нет")

    """Запрос на название вакансии, длина топ-списка"""
    search_query = input("Введите поисковый запрос: ")
    vacancies = []
    for manager in managers:
        for vac in manager.get_vacancies(search_query):
            vacancies.append(vac)
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    min_salary = int(input(("Введите минимальную зарплату для фильтрации: ")))
    filtered_vacancies = VacanciesFilter.filter_by_salary(vacancies, min_salary)
    top_vacancies = VacanciesFilter.get_top_by_salary(filtered_vacancies, top_n)

    while True:
        print_output_variants()
        output_choice = input("Ваш выбор: ")
        if output_choice == '1':
            print_vacancies(sorted(top_vacancies, reverse=True))
            break
        elif output_choice == '2':
            jsonFileManager = JSONFileManager('output.json')
            jsonFileManager.write_file(sorted(top_vacancies, reverse=True))
            break


if __name__ == '__main__':
    user_interaction()
