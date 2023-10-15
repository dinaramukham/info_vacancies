from info_from_API import HeadHunter, Superjob
from vacancies import Vacancy
from func import filtred_salary, get_translet
from save_into_file import SaveInJson

if __name__ == '__main__':
    prof = input('Введите проффесию')
    ans_user = input('Отсортировать по зп?  да|нет')
    # получаем список вакансий
    HeadHunter.change_params(text=prof)
    Superjob.change(keyword=prof)
    hh_prof = HeadHunter.get_json_info()
    sj_prof = Superjob.get_info()
    # получаем сокращенную инфу о вакансиях
    # ввида {'id': __, 'name': __, 'address': __, 'url': __, 'salary': {}, 'requirement': __, 'responsibility': __}
    list1 = []
    list2 = []
    for el in hh_prof:
        vacancy = Vacancy(hh_prof, el, HeadHunter.params)
        list1.append(vacancy.info_dict())
    for el in sj_prof:
        vacancy = Vacancy(sj_prof, el, Superjob.params)
        list2.append(vacancy.info_dict())
    # если без сортировки
    if 'нет' in ans_user.lower():
        print('из hh.ru')
        for el in list1:
            print(f'Вакансия {el}')
        print('из superjob.ru')
        for el in list2:
            print(f'Вакансия {el}')
    # автоматом переводит евро и доллары в рубли, сортирует
    if 'да' in ans_user.lower():
        ans_us = input('по минимальной, по максимальной зп. from|to').strip()
        filt_salary1 = filtred_salary(list1, ans_us)
        filt_salary2 = filtred_salary(list1, ans_us)
        chan_list1 = get_translet(filt_salary1, ans_us)
        chan_list2 = get_translet(filt_salary2, ans_us)
        sort_salary1 = sorted(filt_salary1, key=lambda x: x['salary'][ans_us], reverse=False)
        sort_salary2 = sorted(filt_salary2, key=lambda x: x['salary'][ans_us], reverse=False)
        print('из hh.ru')
        for el in sort_salary1:
            print(el)
        print('из superjob.ru')
        for el in sort_salary2:
            print(el)
    # сохранить в файл. автоматом в 'vacancies.json', если файл существует то в него,
    # если не существует создается
    save_json = input('Сохранить вакансии в файл? да|нет ')
    if 'да' in save_json:
        SaveInJson.add_vacancy(list1)
        SaveInJson.add_vacancy(list2)
    print('Чтобы выйти наберите   ex')
