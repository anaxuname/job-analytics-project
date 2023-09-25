import json
from abc import ABC, abstractmethod


class FileManager(ABC):
    """Класс для работы с файлами"""

    @abstractmethod
    def read_file(self):
        """Метод для записи в файл"""
        pass

    @abstractmethod
    def write_file(self, vacancies):
        """Метод для записи в файл"""
        pass

    @abstractmethod
    def add_vacancies_by_keyword(self, vacancies):
        """Метод для считывания файла"""
        pass

    @abstractmethod
    def delete_vac(self, vacancies):
        """Удаление вакансии из списка"""
        pass


class JSONFileManager(FileManager):
    """Класс для работы с JSON-файлами"""

    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        """Метод для записи в файл"""
        pass

    def write_file(self, vacancies):
        data = []
        for vac in vacancies:
            data.append({
                'title': vac.title,
                'url': vac.url,
                'salary': vac.salary,
                'description': vac.description,
            })
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.write(json.dumps(data, ensure_ascii=False, indent=4))

    @staticmethod
    def add_vacancies_by_keyword(vacancies):
        """Метод для считывания файла"""
        dict_vacancies = []
        for vacancy in vacancies:
            vacancy_dict = {
                'title': vacancy.title,
                'url': vacancy.link,
                'salary': vacancy.get_salary(),
                'description': vacancy.description,
            }
            dict_vacancies.append((vacancy_dict))
        return dict_vacancies

    def delete_vac(self, vacancies):
        """Удаление вакансии из списка"""
        with open(self.filename, 'r', encoding='utf-8') as file:
            to_delete_vac = file.read()
            data = json.loads(to_delete_vac)

    def add_vacancies_by_keyword(self, keyword: dict):
        """Метод для считывания файла"""
        with open(self.filename, 'r', encoding='utf-8') as file:
            data_by_keyword = file.read()
            data = json.loads(data_by_keyword)
            filtered_vacancies = []
            for vacancy in data:
                indicator = True
                for k, v in keyword.items():
                    if k == "salary":
                        if vacancy['salary'] < v:
                            indicator = False
                            break
                if indicator:
                    filtered_vacancies.append(vacancy)
            return filtered_vacancies

class CSVFileManager(FileManager):
    """Класс для работы с CSV-файлами"""
    pass


class ExcelFileManager(FileManager):
    """Класс для работы с Excel-файлами"""
    pass
