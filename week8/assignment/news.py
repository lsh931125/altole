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
    }
}

totalGet = []
totalSoup = []
totalList = []
news = []

def res(a):
    for url in a.values():
        # print(url['url'])
        totalGet.append(requests.get(url['url']))
    return totalGet

def soup(b):
    for soups in b:
        # print(soups)
        totalSoup.append(BeautifulSoup(soups.text,'html.parser'))
    return totalSoup

res(site)
# print(totalGet)
soup(totalGet)
# print(totalSoup)
# findList(totalSoup)

for lists in totalSoup:
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
