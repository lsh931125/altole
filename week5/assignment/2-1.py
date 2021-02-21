
subject = {'korean':80, 'english':75, 'math':55}

def sum(tuple):
    subSum = 0
    for i in tuple:
        subSum = subSum + tuple[i]
    return subSum

def count(tuple):
    subCount = 0
    for i in tuple:
        subCount += 1
    return subCount

total = sum(subject)
subCount = count(subject)
print(f"과목의 합 = {total} 과목의 수 = {subCount} 평균 = {total/subCount}")
