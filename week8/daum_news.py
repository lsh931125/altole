import requests
from bs4 import BeautifulSoup

daumUrl = 'https://search.daum.net/search?w=news&sort=accuracy&q=%EC%BD%94%EB%A1%9C%EB%82%98&cluster=y&DA=STC&dc=STC&pg=1&r=1&p=1&rc=1&at=more&sd=&ed=&period='
res = requests.get(daumUrl)
soup = BeautifulSoup(res.text,'html.parser')
listNews = soup.find_all('a', class_ = 'f_link_b')
print(listNews)

for i in listNews:
    title = i.text
    # print(title)
    link = i.attrs['href']
    # print(link)
    print(f'제목 = {title}\n링크 = {link}')