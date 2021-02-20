# +
# -
# *
# /
# //
# %

# 1~100까지의 숫자중 3의 배수의 합을 출력

sum = 0

for i in range(1,101):
    if i%3 == 0:
        sum += i
    
print(sum)