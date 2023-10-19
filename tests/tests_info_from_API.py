import pytest
from classes.info_from_API import HeadHunter, Superjob


@pytest.fixture()
def hh_analyst():
    return HeadHunter.change_params(text='аналитик')


def tests_HeadHunter():
    assert HeadHunter.params == {'page': 0, 'area': 1, 'per_page': 100}


def tests_HeadHunt():
    assert HeadHunter.url == 'https://api.hh.ru/vacancies'


def tests_hh_params(hh_analyst):
    assert HeadHunter.params['text'] == 'NAME:аналитик'


def tests_hh_get_json_info(hh_analyst):
    assert isinstance(HeadHunter.get_json_info(), list)


@pytest.fixture()
def sj_analyst():
    return Superjob.change(keyword='аналитик')


def tests_Superjob():
    assert Superjob.params == {
        'town': 'Москва',
        'keyword': '',
        'page': 0,
        'count': 100
    }


def tests_sj_change_keyword(sj_analyst):
    Superjob.change(keyword='менеджер')
    assert Superjob.params['keyword'] == 'менеджер'


def tests_sj_change_town(sj_analyst):
    Superjob.change(town='Самара')
    assert Superjob.params['town'] == 'Самара'


def tests_sj_get_info(sj_analyst):
    assert isinstance(Superjob.get_info(), list)
