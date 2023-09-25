class Vacancy:
    """Основной класс для работы с вакансией"""

    def __init__(self, title: str, url: str, salary: int, description: str):
        self.title = title
        self.url = url
        self.salary = int(salary)
        self.description = description

    def __repr__(self):
        return f'Vacancy({self.title}, {self.salary}, {self.description})'

    def __gt__(self, other):
        return self.salary > other.salary

    def __lt__(self, other):
        return self.salary < other.salary


