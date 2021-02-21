def increase(a,b):
    count = 1
    char = a
    while count < b:
        count += 1
        print(char)
        char = char + a
    print(char)

increase('*',5)

