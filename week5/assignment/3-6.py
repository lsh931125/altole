numbers = [1, 2, 3, 4, 5]

def oddMultiTwo(list):
    result = []
    for i in list:
        if i%2 == 1:
            result.append(i*2)
    print(result)

oddMultiTwo(numbers)