# 모듈
# 특정 기능의 집합.
# pip 명령어
# pip는 모듈을 설치하기 위한 명령어

# 모듈 설치
# pip install 모듈명

# 모듈 사용
# import 모듈명

import requests
# requeste http 통신을 할 수 있는 모듈
# requests 안에 있는 Get이라는 함수 사용
# get 함수 첫번째 인자값 요청을 보낼 URL (get이라는 메소드를 이용해서 보냄)

res = requests.get('http://naver.com')


print(res.text)