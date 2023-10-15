from bs4 import BeautifulSoup
import requests
import json


def printj(dict_to_print: dict) -> None  :
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

def filtred_salary(dict_: dict, texts: str):
    """
    :param dict_: список вакансий
    :param texts: 'from' или 'to'
    :return: список вакансий с 'from' или 'to'
    """
    listhh = []
    text=texts.strip()
    for el in range(len(dict_)) :
        if dict_[el]['salary'] == None or dict_[el]['salary'][text] == None:
            continue
        if type(dict_[el]['salary'][text]) == int:
            listhh.append(dict_[el])
    return listhh
def get_course(currency='USD'):
    """
    :param currency: 'USD' или 'RUB'
    :return: int курс
    """
    if currency =='USD':
        IN_RUB='https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
    if currency =='RUB':
        IN_RUB='https://www.google.com/search?q=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&sca_esv=573572359&sxsrf=AM9HkKmvEh2e5rcQAaVLfO6dxqZzR79F3g%3A1697356606734&ei=PpsrZe2-LNKXjgaIpLnwCw&ved=0ahUKEwjt1eeMyveBAxXSi8MKHQhSDr4Q4dUDCBA&uact=5&oq=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lp=Egxnd3Mtd2l6LXNlcnAiFtC10LLRgNC-INC6INGA0YPQsdC70Y4yChAAGIoFGLEDGEMyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgARIryBQ8wNY5BlwAXgAkAEAmAFcoAH9A6oBATa4AQPIAQD4AQHCAgoQABhHGNYEGLADwgIKEAAYigUYsAMYQ8ICBhAAGAcYHsICCBAAGAcYHhgKwgIHEAAYgAQYCuIDBBgAIEGIBgGQBgo&sclient=gws-wiz-serp'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    response=requests.get(IN_RUB , headers= headers  )
    soup=BeautifulSoup(response.content ,  'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    num=float(convert[0].text.replace(',','.'))
    return round(num)
#def get_translet(data, key):
#    pass
#    for el in data:
#        if data[el]['salary']['currency'] ==

