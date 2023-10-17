from abc import ABC, abstractmethod
from thefuzz import fuzz
from classes.info_from_API import HeadHunter
from vacancies import Vacancy
import json


class SaveInFile(ABC):
    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def info_vacancy(self):
        pass

    @abstractmethod
    def del_info_vacancy(self):
        pass


class SaveInJson(SaveInFile):
    @classmethod
    def add_vacancy(cls, vacanсy, name_file='vacancies.json'):
        """
        :param vacanсy: принимает как словарь ввида: vacancy.info_dict(), так и список словарей
        :param name_file: имя создаваемого файла
        :return:
        """
        try: # если файл существует
            with open(name_file) as file:
                data = json.load(file)
            if type(vacanсy) == list:
                for el in vacanсy:
                    data.append(el)
            if type(vacanсy) == dict:
                data.append(vacanсy)
            with open(name_file, 'w') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        except FileNotFoundError: # если не существует создается новый
            data_ = []
            if type(vacanсy) == list:
                for el in vacanсy:
                    data_.append(el)
            if type(vacanсy) == dict:
                data_.append(vacanсy)
            with open(name_file, 'w') as file:
                json.dump(data_, file, indent=4, ensure_ascii=False)

    @classmethod
    def info_vacancy(cls, file_json, criteria=None, message=None):
        """
        :param file_json: из какого файла инфу извлекать
        :param criteria:  возможные критерии 0==имя message== ключевое слово,
        1==зп message== рубли, доллары у вакансий с разных сайтов разные значения,
        :param message: название, название валюты, зп ссылка
        :return:
        """
        
        with open(file_json) as file:
            res = json.load(file)
        if criteria == None:
            return res
        if criteria == 0:  # по имени
            data = []
            for el in res:
                if fuzz.partial_ratio(message, el['name']) >= 50:
                    data.append(el)
            return data

        if criteria == 1:  # salary зп в рублях или не
            data = []
            for el in res:
                if el["salary"] == None:
                    continue
                if el["salary"]["currency"] == message:
                    data.append(el)
            return data

    @classmethod
    def del_info_vacancy(cls, element, file_name):
        """ удаления информации о вакансиях по url"""
        with open(file_name) as file:
            res = json.load(file)
        for el in range(len(res)):
            if res[el]["url"] == element.strip():
                res.pop(el)
                break
        with open(file_name, 'w') as file:
            json.dump(res, file, indent=4)
            return f'вакансия {element} удалена'

