from abc import ABC, abstractmethod
import requests
import os
from dotenv import load_dotenv
from func import printj

class GetAPI(ABC):
    @abstractmethod
    def get_json_info(self, params):
        pass


class HeadHunter(GetAPI):
    """
    для получения инфы с hh.ru
    """
    params = {'page': 0, 'area': 1,
              'per_page': 100}  # area=1 по умолчанию это москва page= Нумерация идёт с нуля, по умолчанию выдаётся первая (нулевая) страница с 100 объектами на странице per_page= колво вакансий на стр
    url = 'https://api.hh.ru/vacancies'

    @classmethod
    def get_json_info(cls, parametrise=params):
        """
        возвращыет словарь json с инфой, каждый элемент вакансия
        """
        list_info = []
        try:
            for num in range(0, 1):  # максимум 2000 экземпляров это до 20
                parametrise['page'] = num
                html_text = requests.get(cls.url, parametrise).json()
                for number in range(0, 100):
                    list_info.append(html_text['items'][number])
            return list_info
        except IndexError:
            return list_info

    @classmethod
    def change_params(cls, text=None, area=None):
        """
         меняет  params
        :param text: название вакансии
        :param area:  по умолчанию ==1 это москва, вводить ТОЛЬКО цифру,  остальные города https://api.hh.ru/areas
        :return:
        """
        if text != None:
            cls.params['text'] = f'NAME:{text}'
        if area != None:
            cls.params['area'] = area


class Superjob(ABC):
    # __api_key: str = os.getenv('API_KEY')
    # order_field	<string:date|payment>	Сортировка: date - по дате публикации, payment - по сумме оклада. По умолчанию - date.
    # order_direction	<string:asc|desc>	Направление сортировки: asc - прямая, desc - обратная. По умолчанию - desc.
    # town	string|int	Название города или его ID
    load_dotenv()

    headers = {
        'X-Api-App-Id': os.getenv('API_KEY'), #
    }
    params = {
        'town': 'Москва',
        'keyword': '',
        'page': 0,
        'count': 100
    }

    @classmethod
    def get_info(cls, parametr=params):
        """выдает лист с вакансиях"""
        list_info = []
        try:
            for el in range(0, 1):  # максимум 500 экземпляров это до 5
                parametr['page'] = el
                data = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=cls.headers,
                                    params=cls.params).json()

                for num in range(0, 100):
                    list_info.append(data["objects"][num])
            return list_info
        except IndexError:
            return list_info

    @classmethod
    def change(cls, keyword=None, town=None):
        """
        :param keyword: ключевое слово в вакансии
        :param town: город.  можно писать название
        :return:
        """
        """ меняет параметр класса: params"""
        if keyword != None:
            cls.params['keyword'] = keyword
        if town != None:
            cls.params['town'] = town
Superjob.change('Python')
print(Superjob.get_info())