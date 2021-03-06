from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver') # 웹드라이버 파일 경로
driver.get("https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%ED%83%9C%EB%AF%BC") # 이미지 검색 URL
time.sleep(5) # 5초 동안 페이지 로딩 기다리며 파이썬은 쉰다.

req = driver.page_source
# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(req, 'html.parser')

# 아까 복사한 Selector를 넣어준다.
thumnails = soup.select_one('#main_pack > section > div._contentRoot.image_wrap > div.photo_group._listGrid > div.photo_tile._grid > div:nth-child(1) > div > div.thumb > a > img')
print(thumnails['src'])


driver.quit() # 끝나면 닫아주기