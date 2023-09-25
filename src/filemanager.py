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


class CSVFileManager(FileManager):
    """Класс для работы с CSV-файлами"""
    pass


class ExcelFileManager(FileManager):
    """Класс для работы с Excel-файлами"""
    pass
