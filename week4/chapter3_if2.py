# if 조건:
# elif 또 다른 조건:
# elif 또 다른 조건:
# elif 또 다른 조건:
# else:  - 위의 조건이 아무것도 부합되지 않을때 실행

money = 30000
if money > 50000:
    print('Taxi')
elif money > 30000:
    print('Train')
elif money > 10000:
    print('Bus')
else:
    print('Walking')

# 조건에 부합하는 경우 뒤에 있는 조건을 실행하지 않는다.

