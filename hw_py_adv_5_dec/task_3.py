import datetime
import json
import logging
import os
import requests
from fake_headers import Headers
from bs4 import BeautifulSoup

def logger(old_function):
    logging.basicConfig(level = logging.INFO, filename = 'task_3_log.log', filemode = 'a', encoding = 'UTF-8')
    def new_function(*args, **kwargs):
        date = datetime.datetime.now()
        log_data = f' дата: {date} имя функции: {old_function.__name__} аргументы: {args} {kwargs}'
        result = old_function(*args, **kwargs)
        log_data = f'{log_data} возвращено: {result}'
        logging.info(log_data)
        return result
    return new_function


def test_3():

    path = 'task_3_log.log'
    if os.path.exists(path):
        os.remove(path)
        
    host = 'https://spb.hh.ru/'
    main = f'{host}search/vacancy?text=python&area=1&area=2'
    words = ('Django','DJANGO','django','Flask','FLASK','flask')

    def g_headers():
        return Headers(browser='firefox', os='win').generate()
    result = []

    @logger
    def ws(item):
        flag = 0
        link = item.find('a',class_='serp-item__title')['href']
        desc = requests.get(link, headers=g_headers()).text
        vac_data = BeautifulSoup(desc, features='lxml')
        vac_name = item.find('a',class_='serp-item__title')
        if vac_name != None:
            vac_name=vac_name.text
        salary = item.find('span',class_='bloko-header-section-3')
        if salary != None:
            salary=salary.text    
        employer = item.find('a',class_='bloko-link bloko-link_kind-tertiary').text
        location = vac_data.find('span',{'data-qa': 'vacancy-view-raw-address'})
        if location != None:
            location=location.text      
        description = vac_data.find('div',{'data-qa': 'vacancy-description'}).text
        for word in words:
            if word in description:
                flag = 1
        if flag == 1:
            res_this = {
                'name':vac_name,
                'salary':salary,
                'employer':employer,
                'location':location,
                'description':description,
            }
            result.append(res_this) 
        return result

    resp = requests.get(main, headers=g_headers())
    resp_t = resp.text
    bs = BeautifulSoup(resp_t, features='lxml')
    vac = bs.find_all('div',class_='vacancy-serp-item-body')

    for item in vac:
        result = ws(item)

    with open('out.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    test_3()