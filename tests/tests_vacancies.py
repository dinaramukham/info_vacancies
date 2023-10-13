from classes.vacancies import  Vacancy
from classes.info_from_API import  HeadHunter,Superjob
import pytest
@pytest.fixture()
def vacan():
    #vac
    HeadHunter.change_params(text= 'аналитик')
    vacancy=Vacancy( HeadHunter.get_json_info(),0, {'page': 0, 'area': 1, 'per_page': 100, 'text': 'NAME:аналитик'})
    return vacancy
@pytest.fixture()
def vacanS():
    #vac
    Superjob.change(keyword=  'аналитик')
    vacancy=Vacancy( Superjob.get_info(),0, Superjob.params )
    return vacancy
def test_vacan_init(vacan):
    assert type(vacan.id)  ==str
    assert type(vacan.name) == str
    assert type(vacan.requirement) == str
    assert type(vacan.responsibility) == str
    assert type(vacan.url) == str
    assert type(vacan.address) is str  or type(None)
    assert type(vacan.salary) is dict or type(None)
def test_vacan_id(vacan):
    data=HeadHunter.get_json_info()
    assert vacan.id == Vacancy.get_vacancy(data)['id']
def test_vacanS_name(vacanS):
    data=Superjob.get_info()
    assert vacanS.name == Vacancy.get_vacancy(data)['profession']
def test_vacanS_salar(vacanS ):
    data=Superjob.get_info()
    salary = {}
    salary['from'] = Vacancy.get_vacancy(data)["payment_from"]
    salary['to'] = Vacancy.get_vacancy(data)["payment_to"]
    salary['currency'] = Vacancy.get_vacancy(data)['currency']
    assert vacanS.salary  == salary
def test_vacanS_address(vacanS):
    data=Superjob.get_info()
    assert vacanS.address  == Vacancy.get_vacancy(data)['address']