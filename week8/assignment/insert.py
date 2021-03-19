import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

site = {
    'naver' : {
        'url' : 'https://search.naver.com/search.naver?where=news&query=%EC%BD%94%EB%A1%9C%EB%82%98&sm=tab_srt&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so%3Ar%2Cp%3Aall%2Ca%3Aall&mynews=0&refresh_start=0&related=0',
        'title' : [],
        'link' : []
    },
    'daum' : {
        'url' : 'https://search.daum.net/search?w=news&sort=accuracy&q=%EC%BD%94%EB%A1%9C%EB%82%98&cluster=y&DA=STC&dc=STC&pg=1&r=1&p=1&rc=1&at=more&sd=&ed=&period=',
        'title' : [],
        'link' : []
    },
    'nine' : {
        'url' : 'https://www.9news.com.au/coronavirus',
        'title' : [],
        'link' : []
    },
    'daily' : {

        'title' : [],
        'link' : []
    }
}

totalGet = []
totalSoup = []
totalList = []

driver = webdriver.Chrome('D:\\altole\\altole\\week8\\chromedriver.exe')

def res(a):
    for url in a.values():
        # print(url['url'])
        if 'url' in url:
            totalGet.append(requests.get(url['url']))
        else:
            url['url'] = 'https://www.dailytelegraph.com.au/search-results/'
            driver.get(url['url'])
            time.sleep(1)
            search = driver.find_element_by_css_selector(".search_box_form .search_box_input")
            time.sleep(1)
            search.click()
            time.sleep(1)
            search.send_keys('corona')
            time.sleep(7)
            page = driver.page_source
            totalGet.append(page)
            # print(url['url'])

    return totalGet

def soup(b):
    for soups in b:
        # print(soups)
        if str(type(soups)) == "<class 'requests.models.Response'>":
            totalSoup.append(BeautifulSoup(soups.text,'html.parser'))
        elif str(type(soups)) == "<class 'str'>":
            totalSoup.append(BeautifulSoup(soups,'html.parser'))
    return totalSoup

def li(c):
    for lists in c:
        totalList = lists.find_all('a', class_ = 'news_tit')
        if totalList is not None:
            for i in totalList:
                site['naver']['link'].append(i.attrs['href'])
                site['naver']['title'].append(i.attrs['title'])
            totalList = []
        
        totalList = lists.find_all('a', class_ = 'story__headline__link')
        if totalList is not None:
            for i in totalList:
                site['nine']['link'].append(i.attrs['href'])
                site['nine']['title'].append(i.text)
            totalList = []

        totalList = lists.find_all('a', class_ = 'f_link_b')
        if totalList is not None:
            for i in totalList:
                site['daum']['link'].append(i.attrs['href'])
                site['daum']['title'].append(i.text)
            totalList = []

        totalList = lists.find_all('a', class_ = 'storyblock_title_link')
        if totalList is not None:
            for i in totalList:
                site['daily']['link'].append(i.attrs['href'])
                site['daily']['title'].append(i.text)
            totalList = []
    return site

res(site)
# print(totalGet)
# print(type(totalGet[0]))
soup(totalGet)
# print(totalSoup[3])
# findList(totalSoup)
li(totalSoup)

# potal = list(site.keys())
# print(potal)
# print(type(potal))

for i in range(0,4):
    if list(site.keys())[i] == 'naver':
        print('naver')
    elif str(site.keys()[i]) == 'daum':
        print('daum')
    elif str(site.keys()[i]) == 'nine':
        print('nine')


# for values in site.values():
#     print(site.keys())
    # if site.keys() == 'naver':
        # print('insert into news(site,title,link) values(\'%s\',\'%s\',\'%s\')' % site['naver']['site'],site['naver']['title'],site['naver']['link'])