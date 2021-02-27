# bs모듈

# html에서 원하는 데이터를 뽑아오는 방법이 크게 2가지.
# 1. 정규식
# 2. DOM접근

# bs 모듈은 HTML DOM에 접근을 하여 원하는 데이터를 가지고 올 수 있게 도와줌.

# import 모듈명
# from 모듈명 import 함수명



import requests
from bs4 import BeautifulSoup

res = requests.get('http://naver.com')
# 첫 번째 인자값 = html내용, 두번째 인자값은 'html.parser'
soup = BeautifulSoup(res.text,'html.parser')   # DOM 접근 가능.

# 태그 접근시 변수명.태그명
# 중복되는 태그가 있는 경우 맨 앞에 태그가 잡힌다. (한개만)
# print(soup.title)

# 텍스트를 가지고 오고싶은경우
# .text
# print(soup.title.text)

# .find('태그명',조건)
# 조건 > id 또는 class의 속성값기준
# class_ = '클래스값'
# id = 'id값'
# print(soup.find('div', id='addiv'))
# 맨 앞의 내용만 가져옴

# .find_all('태그명',조건)
# 리스트 형태로 리턴됨

print(soup.find_all('a', class_='thumb')[0])