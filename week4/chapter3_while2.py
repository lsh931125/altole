# break
# - 깨부시다.
# 반복문을 깨부시고 끝내겠습니다.

# continue
# - 지속하다
# 뒤에있는 소스는 더이상 진행하지 않고 반복문의 맨 처음으로 돌아가겠습니다.

count = 0
while True:
    count = count + 1
    if count == 5:
        continue

    if count == 10:
        break

    print(count)