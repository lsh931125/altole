# import requests
# from bs4 import BeautifulSoup
#
# daily_url = 'https://www.dailytelegraph.com.au/search-results/?q=corona'
# res = requests.get(daily_url)
# print(res)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.dailytelegraph.com.au/search-results/?q=')
# driver.execute_script("document.getElementsByClassName('ais-SearchBox-input search_box_input').value = 'corona'")
driver.find_element_by_xpath('//*[@id="searchInput"]/div/form/input').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="searchInput"]/div/form/input').send_keys('corona')
time.sleep(1)
# print(driver.page_source)
# driver.find_element_by_xpath('//*[@id="searchInput"]/div/form/input').send_keys(Keys.ENTER)




