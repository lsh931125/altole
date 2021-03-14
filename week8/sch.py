# 스케쥴러 모듈
# pip install schedule

import schedule

# 실행 될 함수 정의
def job():
    # 크롤링 하고 DB에 저장하는 소스
    print('Hello')

schedule.every(3).seconds.do(job) # 10초 마다 job이라고 하는 함수를 실행시키겠습니다.

while True:
    schedule.run_pending()
