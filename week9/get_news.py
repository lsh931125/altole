import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pymysql


conn = pymysql.connect(
    host = '', # host name
    user = '', # user name
    password = '', # password
    db = 'crawling', # db name
    charset = 'utf8'
)
curs = conn.cursor()

site = {
    'naver' : {
        'name' : 'naver',
        'url' : 'https://search.naver.com/search.naver?where=news&query=%EC%BD%94%EB%A1%9C%EB%82%98&sm=tab_srt&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so%3Ar%2Cp%3Aall%2Ca%3Aall&mynews=0&refresh_start=0&related=0',
        # 'title' : [],
        # 'link' : [],
        'type' : 'requests'
    },
    'daum' : {
        'name': 'daum',
        'url' : 'https://search.daum.net/search?w=news&sort=accuracy&q=%EC%BD%94%EB%A1%9C%EB%82%98&cluster=y&DA=STC&dc=STC&pg=1&r=1&p=1&rc=1&at=more&sd=&ed=&period=',
        # 'title' : [],
        # 'link' : [],
        'type' : 'requests'
    },
    'nine' : {
        'name': 'nine',
        'url' : 'https://www.9news.com.au/coronavirus',
        # 'title' : [],
        # 'link' : [],
        'type' : 'requests'
    },
    # 'daily' : {
    #     'name': 'daily',
    #     'url' : 'https://www.dailytelegraph.com.au/search-results/?q=corona',
    #     'title' : [],
    #     'link' : [],
    #     'type' : 'selenium'
    # }
}

# 1. HTML 소스를 가지고오는 함수
def getHtml(url, type):
    html = ''

    if (type == 'requests'):
        html = requests.get(url).text
    elif (type == 'selenium'):
        driver = webdriver.Chrome('C:\\Users\\lsh93\\Documents\\html\\altole\\week8\\chromedriver')
        driver.get(url)
        time.sleep(15)
        html = driver.page_source
        driver.close()

    return html

# print(getHtml('http://naver.com','selenium'))

# 2. 뉴스의 링크와 제목을 리턴시켜주는 함수 (범용성을 높임.)
def getNews(name, html):
    bs = BeautifulSoup(html, 'html.parser')
    result = {
        'link' : [],
        'title' : []
    }
    if (name == 'naver'):
        totalList = bs.find_all('a', class_='news_tit')

        for i in totalList:
            result['link'].append(i.attrs['href'])
            result['title'].append(i.attrs['title'])

    elif (name == 'nine'):
        totalList = bs.find_all('a', class_='story__headline__link')

        for i in totalList:
            result['link'].append(i.attrs['href'])
            result['title'].append(i.text)

    elif (name == 'daum'):
        totalList = bs.find_all('a', class_='f_link_b')
        for i in totalList:
            result['link'].append(i.attrs['href'])
            result['title'].append(i.text)

    elif (name == 'daily'):
        totalList = bs.find_all('a', class_='storyblock_title_link')
        for i in totalList:
            result['link'].append(i.attrs['href'])
            result['title'].append(i.text)

    return result

for values in site.values():
    html = getHtml(values['url'], values['type'])
    result = getNews(values['name'], html)
    # site[values['name']]['link'] = result['link']
    # site[values['name']]['title'] = result['title']
    # Insert
    for i in range(0,len(result['title'])):
        # 중복되는 값이 있는지 체크하기.
        # 1. select 해서 값이 이미 존재하는지 확인.
        # 값이 이미 존재한다면 Update
        # 값이 존재하지 않으면 Insert.
        sql = "select * from news where link = %s"
        curs.execute(sql, (result['link'][i]))
        select_result = curs.fetchall()

        if (len(select_result) > 0):
            # update
            sql = "update news set title = %s where link = %s"
            curs.execute(sql, (result['title'][i],result['link'][i]))
        else:
            # insert
            sql = "insert into news(site,title,link) values(%s,%s,%s)"
            curs.execute(sql, (values['name'], result['title'][i],result['link'][i]))
    conn.commit()

