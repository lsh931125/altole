from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.dailytelegraph.com.au/search-results')
search = driver.find_element_by_css_selector(".search_box_form .search_box_input")
time.sleep(3)
search.click()
time.sleep(3)
search.send_keys('corona')
time.sleep(7)

news = driver.find_elements_by_css_selector('article.storyblock')
# print(news)
for i in news:
    title = i.find_element_by_css_selector('a.storyblock_title_link').text
    link = i.find_element_by_css_selector('a.storyblock_title_link').get_attribute('href')
    print(f'제목 = {title}\n링크 = {link}')