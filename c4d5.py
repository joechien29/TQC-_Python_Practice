d = int(input())

while d != -9999:
    if 90 <= d <= 100:
        print('A')
    elif 80 <= d <= 89:
        print('B')
    elif 70 <= d <= 79:
        print('C')
    elif 60 <= d <= 69:
        print('D')
    elif 0 <= d <= 59:
        print('E')
    d = int(input())
