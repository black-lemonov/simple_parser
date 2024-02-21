import requests
from bs4 import BeautifulSoup as BS

"""More libraries for parsing: Scrapy, lxml"""

r = requests.get('https://ria.ru/person_Boris_Nadezhdin+politics/')
r.encoding = 'UTF8'
html = BS(r.content, 'html.parser')

# GET request:
# https://ria.ru/services/politics/more.html?id=1927955948&date=20240217T145439

for article in html.select('.list-item__content'):
    print(article.text)
else:
    print('page #2')
    r = requests.get('https://ria.ru/services/politics/more.html?')
    print(r.status_code)
    for article in html.select('.list-item__content'):
        print(article.text)