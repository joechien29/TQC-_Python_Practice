d = int(input())

while d != 0:
    if d == 0:
        print(d)
    else:
        print(d % 10, end='')
        d //= 10
