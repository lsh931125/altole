import requests
from bs4 import BeautifulSoup

naverUrl = 'https://search.naver.com/search.naver?where=news&query=%EC%BD%94%EB%A1%9C%EB%82%98&sm=tab_srt&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so%3Ar%2Cp%3Aall%2Ca%3Aall&mynews=0&refresh_start=0&related=0'
res = requests.get(naverUrl)
soup = BeautifulSoup(res.text, 'html.parser')
listNews = soup.find_all('a', class_ = 'news_tit')
# print(listNews)

for i in listNews:
    link = i.attrs['href']
    # print(link)
    title = i.attrs['title']
    # print(title)
    print(f'제목 = {title}\n링크 = {link}')
