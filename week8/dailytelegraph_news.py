# import requests
# from bs4 import BeautifulSoup
#
# daily_url = 'https://www.dailytelegraph.com.au/search-results/?q=corona'
# res = requests.get(daily_url)
# print(res)

from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.dailytelegraph.com.au/search-results/?q=covid')
print(driver.page_source)