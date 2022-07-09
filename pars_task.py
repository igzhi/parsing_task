import requests
from bs4 import BeautifulSoup

url_a = 'https://habr.com'
url = url_a + '/ru/all/'
KEYWORDS = ['bloomberg', 'пояснице', 'ISO', 'Unity', 'python', 'тестировщик']
headers = {'User-Agent' : 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, features='html.parser')
el = soup.find_all(class_='tm-articles-list__item')

for element in el:

    i = element.find(class_='article-formatted-body article-formatted-body article-formatted-body_version-2')
    if i is not None:
        ii = i.text
    else:
        continue

    time = element.find('time').text
    article = element.find('h2').find('span').text
    hyper = element.find(class_='tm-article-snippet__title-link').attrs['href']
    for key in KEYWORDS:
        if key.lower() in ii.lower():
            print(f'\n{article}, \nНовость опубликована:{time}, \nСсылка на новость: {url_a+hyper}')


