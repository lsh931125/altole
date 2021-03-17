# import requests

#
# daily_url = 'https://www.dailytelegraph.com.au/search-results/?q=corona'
# res = requests.get(daily_url)
# print(res)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('D:\\altole\\altole\\week8\\chromedriver.exe')
driver.get('https://www.dailytelegraph.com.au/search-results/')
search = driver.find_element_by_css_selector(".search_box_form .search_box_input")
time.sleep(3)
search.click()
time.sleep(3)
search.send_keys('corona')
time.sleep(7)

page = driver.page_source
print(type(page))
# print(news)
soup = BeautifulSoup(page,'html.parser')
# print(soup)
listNews = soup.find_all('a', class_ = 'storyblock_title_link')
# print(listNews[0].text)

for i in listNews:
    title = i.text
    link = i.attrs['href']
    print(f'제목 = {title}\n링크 = {link}')