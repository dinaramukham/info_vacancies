from info_from_API import HeadHunter, Superjob
from vacancies import Vacancy
from func import filtred_salary, get_translet
from save_into_file import SaveInJson

if __name__ == '__main__':
    while True:
        profession = input('Введите проффесию')
        ans_user = input('Отсортировать по зп?  да|нет')
        # получаем список вакансий
        HeadHunter.change_params(text=profession)
        Superjob.change(keyword=profession)
        hh_prof = HeadHunter.get_json_info()
        sj_prof = Superjob.get_info()
        # получаем сокращенную инфу о вакансиях
        # ввида {'id': __, 'name': __, 'address': __, 'url': __, 'salary': {}, 'requirement': __, 'responsibility': __}
        list_hh = []
        list_sj = []
        for number in range(len(hh_prof)):
            vacancy = Vacancy(hh_prof, number, HeadHunter.params)
            list_hh.append(vacancy.info_dict())
        for number in range(len(sj_prof)):
            vacancy = Vacancy(sj_prof, number, Superjob.params)
            list_sj.append(vacancy.info_dict())
        # если без сортировки
        if 'нет' in ans_user.lower():
            print('из hh.ru')
            for vacancy in list_hh:
                print(f'Вакансия {vacancy}')
            print('из superjob.ru')
            for vacancy in list_sj:
                print(f'Вакансия {vacancy}')
        # автоматом переводит евро и доллары в рубли, сортирует
        if 'да' in ans_user.lower():
            ans_us = input('по минимальной, по максимальной зп. from|to').strip()
            print('*указання зп будет в рублях*')
            filt_salary_hh = filtred_salary(list_hh, ans_us)
            filt_salary_sj = filtred_salary(list_sj, ans_us)
            chan_list_hh = get_translet(filt_salary_hh, ans_us)
            chan_list_sj = get_translet(filt_salary_sj, ans_us)
            sort_salary1 = sorted(chan_list_hh, key=lambda x: x['salary'][ans_us], reverse=False)
            sort_salary2 = sorted(chan_list_sj, key=lambda x: x['salary'][ans_us], reverse=False)
            print('из hh.ru')
            for vacancy in sort_salary1:
                print(vacancy)
            print('из superjob.ru')
            for vacancy in sort_salary2:
                print(vacancy)
        # сохранить в файл. автоматом в 'vacancies.json', если файл существует то в него,
        # если не существует создается
        save_json = input('Сохранить вакансии в файл? да|нет ')
        if 'да' in save_json.lower():
            SaveInJson.add_vacancy(list_hh)
            SaveInJson.add_vacancy(list_sj)
        us_an = input('Чтобы выйти наберите ex иначе пробел')
        if 'ex' in us_an:
            break
