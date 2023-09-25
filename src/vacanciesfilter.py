from src.vacancies import Vacancy


class VacanciesFilter:
    """Класс для сбора топ-N вакансий по параметру salary"""

    @staticmethod
    def filter_by_salary(vacancies: list[Vacancy], value) -> list[Vacancy]:
        result = []
        for vac in vacancies:
            if vac.salary >= value:
                result.append(vac)
        return result

    @staticmethod
    def get_top_by_salary(vacancies: list[Vacancy], value) -> list[Vacancy]:
        return vacancies[:value]