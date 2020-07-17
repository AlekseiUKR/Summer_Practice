import requests
import re

URL = 'http://www.st-petersburg.vybory.izbirkom.ru/region/st-petersburg?action=ik'

def get_html(url):
    r = requests.get(url, params=None)
    return r

def get_contact(html):
    regex = '<td>\d+</td><td><nobr>[А-Яа-я ]+</nobr></td><td>[А-Яа-я/.]+</td><td>[А-Яа-яё -/"&ndash/;]+</td>'
    lst =[]
    res = re.findall(regex,html)
    for j in res:
        reg = re.sub("(<td>|<nobr>|</nobr>|&ndash;)","" ,j)
        reg = re.sub("(</td>)","|" ,reg)
        print(reg)
        lst.append(reg)
def parse():
    URL = input('Введите URL')
    URL = URL.strip()
    html = get_html(URL)
    if html.status_code == 200:
        get_contact(html.text)

    else:
        print("Error")

parse()
