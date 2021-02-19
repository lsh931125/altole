# 흔히 배열이라고 한다. 파이썬에서는 리스트라고 얘기한다.
# 변수명 = [들어갈값1,들어갈값2...]

fruitList = ['apple','banana','orange']
priceList = [3000,5000,4000]

# 값에 접근할때는 변수명[인덱스번호]
# 인덱스 번호 : 몇번째에 있는지 알려주는 번호
# 인덱스 번호는 0부터 시작. 모든언어도 동일

print(fruitList[1])

fruitList[1] = 'pineapple'
print(fruitList[1])