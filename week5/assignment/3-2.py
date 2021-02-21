def multipleThree(num):
    a = 0
    sum = 0
    while a < num:
        a += 1
        if a%3 == 0:
            sum += a
        
    print(sum)

multipleThree(1000)