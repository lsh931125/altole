import requests
from bs4 import BeautifulSoup

naver_url = 'https://search.naver.com/search.naver?where=news&query=%EC%BD%94%EB%A1%9C%EB%82%98&sm=tab_srt&sort=1&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so%3Add%2Cp%3Aall%2Ca%3Aall&mynews=0&refresh_start=0&related=0'
res = requests.get(naver_url)
soup = BeautifulSoup(res.text, 'html.parser')
listNews = soup.find_all('a', class_ = 'news_tit')
print(listNews)
# coronaNews = {}
# num = 1

for i in listNews:
    href = i.attrs['href']
    title = i.attrs['title']
    print(f'제목 = {title} \n 링크 = {href}')
    # coronaNews[num] = '제목 = '+title+'링크 = '+href
    # num += 1
# print(coronaNews[1])
