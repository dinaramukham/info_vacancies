from abc import ABC, abstractmethod
from thefuzz import fuzz
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
        try:  # если файл существует
            with open(name_file) as file:
                data = json.load(file)
            if isinstance(vacanсy, list):
                for one_vacanсy in vacanсy:
                    data.append(one_vacanсy)
            if isinstance(vacanсy, dict):
                data.append(vacanсy)
            with open(name_file, 'w') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        except FileNotFoundError:  # если не существует создается новый
            data_ = []
            if isinstance(vacanсy, list):
                for one_vacanсy in vacanсy:
                    data_.append(one_vacanсy)
            if isinstance(vacanсy, dict):
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
            data = json.load(file)
        if criteria is None:
            return data
        if criteria == 0:  # по имени
            data = []
            for one_vacanсy in data:
                if fuzz.partial_ratio(message, one_vacanсy['name']) >= 50:
                    data.append(one_vacanсy)
            return data

        if criteria == 1:  # salary зп в рублях или не
            data = []
            for one_vacanсy in data:
                if one_vacanсy["salary"] is None:
                    continue
                if one_vacanсy["salary"]["currency"] == message:
                    data.append(one_vacanсy)
            return data

    @classmethod
    def del_info_vacancy(cls, url_vacancy, file_name):
        """ удаления информации о вакансиях по url"""
        with open(file_name) as file:
            data = json.load(file)
        for one_vacanсy in range(len(data)):
            if data[one_vacanсy]["url"] == url_vacancy:
                data.pop(one_vacanсy)
                break
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)
            return f'вакансия {url_vacancy} удалена'
