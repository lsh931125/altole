# 조건이 2개 이상
# 가능하면 조건은 최소화
# AND 연산자
# -> 모든 조건이 참 인경우에만 참
# OR 연산자
# -> 하나의 조건만 참이여도 참

# TRUE AND TRUE : TRUE
# TRUE AND FALSE : FALSE
# TRUE OR TRUE : TRUE
# TRUE OR FALSE : TRUE

a = 3
b = 5
c = 4

if (a < b or b == c) and b > c:
    print('Hello')