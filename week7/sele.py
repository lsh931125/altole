# seleninum
# 브라우저 컨트롤
# 브라우저에서 HTTP 요청을 보낸 다음 HTML을 가지고 오는게 우리의 현재 사용목적
# HTTP요청을 파이썬에서 즉시 보낼수 있지만 시고서(HTTP HEADER)를 조작하기 번거롭기 때문에
# 브라우저를 켜서 요청을 보내 실제 사람이 요청한것처럼 꾸민다. - 셀레니움을 사용하는 목적

# 장점 : 신고서 작성을 안해도 알아서 들어가있기때문에 편하다
# 단점 : 속도가 단순 HTTP 요청보다 느리다.

# pip install selenium

# requests 모듈가지고 HTTP요청을 보내 HTML을 받았는데 원하는 HTML내용이 없는 경우
# selenium 모듈을 사용해서 가지고 오면 보일 수 있다.

from selenium import webdriver
driver = webdriver.Chrome('./chromedriver.exe')

driver.get('http://naver.com')
print(driver.page_source)