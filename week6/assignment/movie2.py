import dload
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver')
driver.get('http://www.naver.com')
time.sleep(5)
