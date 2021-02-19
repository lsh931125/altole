# while 반복문
# 실수하면 무한 루프에 빠지기때문에 조심.
# 개발자가 의도적으로 무한루프에 빠지게끔하는 경우도 있음.

# while 조건:
#   조건이 부합되면 실행될 소스

count = 0
while count < 10:
    count += 1
    print(count)