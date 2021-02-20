# if, elif, else

# if 조건:
#   조건이 부합되는 경우 실행될 소스
# elif 조건:
#   조건이 부합되는 경우 실행될 소스
# elif 조건:
#   조건이 부합되는 경우 실행될 소스
# else:
#   위 조건들이 모두 부합되지 않은 경우 실행 될 소스

# 경우의 수가 많이 나오는 조건을 맨 위로.

money = 30000

if money > 50000:
    print('호텔뷔페')
elif money > 20000:
    print('고기뷔페')
elif money > 5000:
    print('편의점')
else:
    print('집에간다.')