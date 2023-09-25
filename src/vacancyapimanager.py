import os
from abc import ABC, abstractmethod

import requests

from src.vacancies import Vacancy


class VacancyAPIManager(ABC):
    """Класс для работы с API"""
    BASE_URL = ""

    @abstractmethod
    def get_vacancies(self, text: str) -> list[Vacancy]:
        """Метод получает вакансии"""
        pass

    @abstractmethod
    def format_vacancies(self, vac: dict) -> Vacancy:
        """Метод форматирует вакансии в едином формате"""
        pass


class HeadHunterAPIManager(VacancyAPIManager):
    """Класс для работы с API для HeadHunter"""
    BASE_URL = "https://api.hh.ru"

    def get_vacancies(self, text) -> list[Vacancy]:
        path = "/vacancies"
        results = requests.get(self.BASE_URL + path, params={'text': text,
                                                             'order_by': 'salary_desc',
                                                             'area': '1'})
        results = results.json().get('items')
        vacancies = []
        for result in results:
            vacancies.append(self.format_vacancies(result))

        return vacancies

    def format_vacancies(self, vac) -> Vacancy:
        # TODO: currency conversion API
        salary = vac['salary'] if vac['salary'] else {}
        salary = salary['from'] if salary.get('from') else 0
        return Vacancy(vac['name'],
                       vac['alternate_url'],
                       salary,
                       vac['snippet']["requirement"])


class SuperJobAPIManager(VacancyAPIManager):
    """Класс для работы с API для SuperJob"""
    BASE_URL = "https://api.superjob.ru/2.0"

    def get_vacancies(self, text) -> list[Vacancy]:
        path = "/vacancies/"
        headers = {
            'Host': 'api.superjob.ru',
            'X-Api-App-Id': os.getenv("SJ_API_KEY"),
            'Authorization': 'Bearer r.000000010000001.example.access_token',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        results = requests.get(self.BASE_URL + path, params={'keyword': text}, headers=headers)
        results = results.json().get('objects')
        vacancies = []
        for result in results:
            vacancies.append(self.format_vacancies(result))

        return vacancies

    def format_vacancies(self, vac) -> Vacancy:
        salary = vac['payment_from'] if vac.get('payment_from') else 0
        return Vacancy(vac['profession'],
                       vac['link'],
                       salary,
                       vac['work'])

