import requests
from bs4 import BeautifulSoup

nine_url = 'https://www.9news.com.au/coronavirus'
res = requests.get(nine_url)
soup = BeautifulSoup(res.text,'html.parser')
listNews = soup.find_all('a', class_ = 'story__headline__link')
# print(listNews)

for i in listNews:
    title = i.text
    # print(title)
    link = i.attrs['href']
    # print(link)
    print(f'제목 = {title}\n링크 = {link}')