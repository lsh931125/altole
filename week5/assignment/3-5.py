classScore = [70,60,55,75,95,90,80,80,85,100]

def avg(list):
    total = 0
    count = 0

    for i in list:
        total += i
        count += 1
    print(total/count)

avg(classScore)