from classes.info_from_API import HeadHunter, Superjob

from func import filtred_salary

class Vacancy():
    """важно следить за HeadHunter.params, при их замене меняется вывод HeadHunter.get_json_info()"""
    def __init__(self, data, number_vacancy, params): # HeadHunter.change_params(text= 'аналитик') сначала вводим профессию
        self.number_vacancy=number_vacancy     # vacancy=Vacancy( HeadHunter.get_json_info(),1,HeadHunter.params)
        self.params=params
        self.id = Vacancy.get_vacancy(data, self.number_vacancy)['id']
        try: # если HeadHunter
            self.name= Vacancy.get_vacancy(data, self.number_vacancy)["name"]
            self.requirement=Vacancy.get_vacancy(data, self.number_vacancy)["snippet"]["requirement" ]
            self.responsibility=Vacancy.get_vacancy(data, self.number_vacancy)["snippet"]["responsibility"]
            self.url=Vacancy.get_vacancy(data, self.number_vacancy)['alternate_url']
            if Vacancy.get_vacancy(data, self.number_vacancy)['address']==None :
                self.address=None
            else:
                self.address= Vacancy.get_vacancy(data, self.number_vacancy)['address']['raw']
            if Vacancy.get_vacancy(data, self.number_vacancy)['salary'] == None:
                self.salary=None
            if type(Vacancy.get_vacancy(data, self.number_vacancy)['salary'])==dict :
                self.salary = {}
                self.salary['from'] = Vacancy.get_vacancy(data, self.number_vacancy)['salary']['from']
                self.salary['to'] = Vacancy.get_vacancy(data, self.number_vacancy)['salary']['to']
                self.salary['currency'] = Vacancy.get_vacancy(data, self.number_vacancy)['salary']['currency']
        except KeyError : # если Superjob
            #self.id = Vacancy.get_vacancy(data, self.number_vacancy)['id']
            self.name = Vacancy.get_vacancy(data, self.number_vacancy)['profession']
            self.requirement = None #Vacancy.get_vacancy(data, self.number_vacancy)["snippet"]["requirement"]
            self.responsibility = Vacancy.get_vacancy(data, self.number_vacancy)["candidat"]
            self.url = Vacancy.get_vacancy(data, self.number_vacancy)["link"]
            if Vacancy.get_vacancy(data, self.number_vacancy)['address'] == None:
                self.address = None
            else:
                self.address = Vacancy.get_vacancy(data, self.number_vacancy)['address']
            self.salary = {}
            self.salary['from'] = Vacancy.get_vacancy(data, self.number_vacancy)["payment_from"]
            self.salary['to'] = Vacancy.get_vacancy(data, self.number_vacancy)["payment_to"]
            self.salary['currency'] = Vacancy.get_vacancy(data, self.number_vacancy)['currency']
    def __str__(self):
        return f"Название вакансии {self.name}, ссылка {self.url}, зп {self.salary}"
    def __repr__(self):
        return f"Vacancy( название {self.name  }, зп {self.salary  },ссылка{self.url  }"

    def info_dict(self):
        """ про одну вакансию инфаf"""
        data={}
        data['id']=self.id
        data['name'] = self.name
        data['address'] = self.address
        data['url'] = self.url
        data['salary'] = self.salary
        data['requirement'] = self.requirement
        data['responsibility'] = self.responsibility
        return data

    @classmethod
    def not_none(cls,one, two):
        """ тупо для сравнения зп"""
        if not isinstance(two, Vacancy):
            raise ValueError
        if  one.salary==None   :
            raise  TypeError
        if two.salary==None:
            raise TypeError
    def __lt__(self, other): # в рублях
        try:
            Vacancy.not_none(self, other)
        except ValueError:
            return 'только экземпляры класса Vacancy'
        except TypeError:
            return 'где то не указана зп'
        else:
            if self.salary['to'] == None and other.salary['from'] == None:
                return self.salary['from'] < other.salary['to']
            if not self.salary['to'] == None and not other.salary['from'] == None:
                return self.salary['to'] < other.salary['from']
            if self.salary['to'] == None:
                return self.salary['from'] < other.salary['from']
            if other.salary['from'] == None:
                return self.salary['to'] < other.salary['to']

    def __le__(self, other):
        try:
            Vacancy.not_none(self, other)
        except ValueError:
            return 'только экземпляры класса Vacancy'
        except TypeError:
            return 'где то не указана зп'
        else:
            if self.salary['to'] == None and other.salary['from'] == None:
                return self.salary['from'] <= other.salary['to']
            if not self.salary['to'] == None and not other.salary['from'] == None:
                return self.salary['to'] <= other.salary['from']
            if self.salary['to'] == None:
                return self.salary['from'] <= other.salary['from']
            if other.salary['from'] == None:
                return self.salary['to'] <= other.salary['to']
    def __eg__(self, other):
        try:
            Vacancy.not_none(self, other)
        except ValueError:
            return 'только экземпляры класса Vacancy'
        except TypeError:
            return 'где то не указана зп'
        else:
            if self.salary['from'] == None and other.salary['from'] == None:
                return self.salary['to'] == other.salary['to']
            if self.salary['from'] == None or other.salary['from'] == None:
                return None # сравнение некоректно, т.к одно из значений None
            if not self.salary['from'] == None and not other.salary['from'] == None:
                return self.salary['from'] == other.salary['from']

    @classmethod
    def get_vacancy(cls, data, index=0):
        """ выдает одну вакансию по индексу """
        return data[index]

Superjob.change(keyword= 'разработчик')
HeadHunter.change_params(text= 'аналитик')
vacancy=Vacancy( Superjob.get_info()  ,6,Superjob.params)
vacancy1=Vacancy( HeadHunter.get_json_info()   ,6,HeadHunter.params)
#list0=[]
#for el in range(0,10):
#    vacancy=Vacancy(HeadHunter.get_json_info(), el, HeadHunter.params)
#    vacancy.info_dict()
#    list0.append(vacancy.info_dict())
#list2=filtred_salary(list0, 'from' )

#a=sorted(list2 ,key=lambda x: x['salary']['from'],reverse=False)
#for el in range(len(a)) :
#    print(a[el ]['salary']['from'])
print(vacancy.info_dict()   )
print(vacancy1.info_dict()   )