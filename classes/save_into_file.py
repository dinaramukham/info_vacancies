from abc import ABC,  abstractmethod
from thefuzz import fuzz
from classes.info_from_API import HeadHunter
from vacancies import  Vacancy
import json
class SaveInFile(ABC ):
    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def info_vacancy(self):
        pass

    @abstractmethod
    def del_info_vacancy(self):
        pass
class   SaveInJson(SaveInFile ):
    @classmethod
    def add_vacancy(cls, vacanсy, name_file='vacancies.json' ):
        """
        :param vacanсy: принимает как словарь ввида: vacancy.info_dict(), так и список словарей
        :param name_file: имя создаваемого файла
        :return:
        """
        with open(name_file) as file:
            data = json.load(file)
        if type(vacanсy)==list:
            for el in vacanсy:
                data.append(el)
        if type(vacanсy)==dict:
            data.append(vacanсy )
        with open(name_file, 'w') as file:
            json.dump(data, file, indent=4 )

    @classmethod
    def info_vacancy(cls, file_json, criteria=None, message=None  ):
        """
        :param file_json: из какого файла инфу извлекать
        :param criteria:  возможные критерии 0==имя, 1==зп, 2==ссылка
        :param message: название, название валюты, зп ссылка
        :return:
        """
        with open(file_json  ) as file:
            res=json.load(file )
        if criteria ==None:
            return res
        if criteria == 0:   #по имени
            data=[]
            for el in res:
                if fuzz.partial_ratio(message , el['name'] )>=50:
                    data.append(el )
            return data
        if criteria == 1: # salary зп в рублях или не
            data = []
            for el in res:
                if  el["salary"]["currency"] == message :
                    data.append(el)
            return data
        if criteria == 2:   #по ссылке
            data=[]
            for el in res:
                if  el["url"] == message :
                    data.append(el )
            return data
    @classmethod
    def del_info_vacancy(cls, element, file_name):
        """ удаления информации о вакансиях по url"""
        with open(file_name  ) as file:
            res=json.load(file )
        for el in range(len(res )) :
            if res[el]["url"]==element:
                res.pop(el )
                break
        with open(file_name, 'w') as file:
            json.dump(res, file, indent= 4  )
            return f'вакансия {element} удалена'
#list0=[]
#for el in range(0,3):
#    vacancy=Vacancy(HeadHunter.get_json_info(), el, HeadHunter.params)
#    vacancy.info_dict()
#    list0.append(vacancy.info_dict())
#for el in list0:
#    print(el )
#SaveInJson.add_vacancy(list0 )
#for el in SaveInJson.info_vacancy('vacancies.json'):
#    print(el )
#print(fuzz.partial_ratio('Здесь будем искать упоминание Cloud!', 'сloudуууу.'))
#print(SaveInJson.info_vacancy('vacancies.json'))
#SaveInJson.del_info_vacancy("https://hh.ru/vacancy/79878614",'vacancies.json')