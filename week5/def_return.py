def len(list):
    count = 0
    for i in list:
        count += 1

    return count

def total(list):
    total = 0
    for i in list:
        total += i

    return total


scoreList = [100,50,60,30,50]
size = len(scoreList)
scoreTotal = total(scoreList)

print(scoreTotal / size)