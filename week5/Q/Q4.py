# 홀수인지 짝수인지 판별
# 함수 사용

# 홀수인지 짝수인지 판별해주는 함수
def odd(number):
    result = ""

    if number%2 == 0:
        result ="짝수"
    elif number%2 == 1:
        result = "홀수"
    
    return result

a = odd(12)
print(a)