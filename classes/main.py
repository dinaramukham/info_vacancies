from info_from_API import HeadHunter,Superjob
from vacancies import Vacancy
from func import filtred_salary
from save_into_file import SaveInJson
if __name__=='__main__':
    prof=input('Введите проффесию')
    ans_user = input('Отсортировать по зп?  да|нет')
    HeadHunter.change_params(text=prof  )
    Superjob.change(keyword=prof  )
    hh_prof=HeadHunter.get_json_info()
    sj_prof=Superjob.get_info()

    list1=[]
    list2 = []
    for  el in hh_prof:
        vacancy=Vacancy(hh_prof, el, HeadHunter.params  )
        list1.append(vacancy.info_dict())
    for  el in sj_prof:
        vacancy=Vacancy(sj_prof , el, Superjob.params  )
        list2.append(vacancy.info_dict())

    if 'нет' in ans_user.lower():
        print('из hh.ru')
        for el in list1 :
            print(f'Вакансия {el}')
        print('из superjob.ru')
        for el in list2:
            print(f'Вакансия {el}')
    # перебирать не list_salary а list2
    if 'да' in ans_user.lower() :
        ans_us=input('по минимальной, по максимальной зп. from|to').strip()
        filt_salary1=filtred_salary(list1 , ans_us )
        filt_salary2 = filtred_salary(list1, ans_us)
        list_s1=sorted(filt_salary1  ,key=lambda x: x['salary'][ans_us ],reverse=False)
        list_s2 = sorted(filt_salary2, key=lambda x: x['salary'][ans_us], reverse=False)
        print('из hh.ru')
        for el in list1 :
            print(el  )
        print('из superjob.ru')
        for el in list1 :
            print(el  )
    print('Чтобы выйти наберите   ex')
    save_json=input('Сохранить вакансии в файл? да|нет ')
    if 'да' in save_json:
        SaveInJson.add_vacancy(list1)
        SaveInJson.add_vacancy(list1)


