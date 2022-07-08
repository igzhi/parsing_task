"""Необходимо парсить страницу со свежими статьями (вот эту) и выбирать те статьи, в которых встречается хотя бы одно из ключевых слов (эти слова определяем в начале скрипта).
Поиск вести по всей доступной preview-информации (это информация, доступная непосредственно с текущей страницы).
Вывести в консоль список подходящих статей в формате: <дата> - <заголовок> - <ссылка>."""

import requests
from bs4 import BeautifulSoup

url_a = 'https://habr.com'
url = url_a + '/ru/all/'
KEYWORDS = ['bloomberg', 'фото', 'web', 'python', 'тестировщик']
headers =  { 'User-Agent' : 'Mozilla/5.0' }

response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.text, features='html.parser')
el = soup.find_all(class_='tm-articles-list__item')

for element in el:
    i = element.find(class_='article-formatted-body article-formatted-body article-formatted-body_version-2').find('p').text
    time = element.find('time').text
    article = element.find('h2').find('span').text
    hyper = element.find(class_='tm-article-snippet__title-link').attrs['href']
    for key in KEYWORDS:
        if key.lower() in i.lower():
            print(f'Новость опубликована: {time}, \n{article}, \nСсылка на новость: {url_a+hyper} \n')


