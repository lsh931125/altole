import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pymysql


conn = pymysql.connect(
    host = '3.35.236.237',
    user = 'root',
    password = 'Hoho4026!',
    db = 'crawling',
    charset = 'utf8'
)
curs = conn.cursor()

site = {
    'naver' : {
        'name' : 'naver',
        'url' : 'https://search.naver.com/search.naver?where=news&query=%EC%BD%94%EB%A1%9C%EB%82%98&sm=tab_srt&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so%3Ar%2Cp%3Aall%2Ca%3Aall&mynews=0&refresh_start=0&related=0',
        'type' : 'requests'
    },
    'daum' : {
        'name' : 'daum',
        'url' : 'https://search.daum.net/search?w=news&sort=accuracy&q=%EC%BD%94%EB%A1%9C%EB%82%98&cluster=y&DA=STC&dc=STC&pg=1&r=1&p=1&rc=1&at=more&sd=&ed=&period=',
        'type' : 'requests'
    },
    'nine' : {
        'name' : 'nine',
        'url' : 'https://www.9news.com.au/coronavirus',
        'type' : 'requests'
    },
    'daily' : {
        'name' : 'daily',
        'url' : '',
        'type' : 'selenium'
    }
}

# 1. html 정보 가져오기
# 2. 가져온 html 정보를 soup
#

# html 정보 가져오기
def getHtml(url, type):
    html = ''

    if (type == 'requests'):
        html = requests.get(url).text
    elif (type == 'selenium'):
        print(type)

    return html

# 2. 가져온 html 정보를 soup
def getNews(name, html):
    news = {
        'title' : [],
        'link' : []
    }
    bs = BeautifulSoup(html, 'html.parser')
    if (name == 'naver'):
        bsList = bs.find_all('a', class_='news_tit')
        for i in bsList:
            news['title'].append(i.attrs['title'])
            news['link'].append(i.attrs['href'])
    elif (name == 'daum'):
        bsList = bs.find_all('a', class_='f_link_b')
        for i in bsList:
            news['title'].append(i.text)
            news['link'].append(i.attrs['href'])
    elif (name == 'nine'):
        bsList = bs.find_all('a', class_='story__headline__link')
        for i in bsList:
            news['title'].append(i.text)
            news['link'].append(i.attrs['href'])

    return news


for i in site.values():
    html = getHtml(i['url'],i['type'])
    news = getNews(i['name'],html)
    # print(news)

    for j in range(0, len(news['title'])):
        selectSql = 'select * from news where link = %s'
        curs.execute(selectSql, (news['link'][j]))
        selectResult = curs.fetchall()

        if (len(selectResult) > 0):
            updateSql = 'update news set title = %s where link = %s'
            curs.execute(updateSql, (news['title'][j],news['link'][j]))
        else:
            insertSql = 'insert into news(site,title,link) values(%s,%s,%s)'
            curs.execute(insertSql, (i['name'],news['title'][j],news['link'][j]))
    conn.commit()