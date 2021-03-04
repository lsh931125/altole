import dload
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver')
driver.get('https://movie.naver.com/movie/running/current.nhn')
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req,'html.parser')
thumbnails = soup.select('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li > div > a > img')
i = 1
for thumbnail in thumbnails:
    img = thumbnail['src']
    print(img)
    dload.save(img,f'img/{i}.jpg')
    i += 1

driver.quit()