# break : 부시다/멈추다
# continue : 지속하다

count = 0
while True: # 무한루프
    count = count + 1 # count에 1씩 누적

    if count == 5:  # 만약 count가 5가 되면
        continue    # 뒤에 있는 소스는 더 이상 진행시키지 않고 반복문 처음으로
    
    if count == 10: # 만약 count가 10이 되면
        break       # 정지

    print(count)    # 카운트 변수의 값 출력