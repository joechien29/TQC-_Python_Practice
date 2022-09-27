n = int(input())

for i in range(1, n+1):
    tmp = 1
    count = 0
    for j in range(n, i-1, -1):
        count += 1
        print('{:<4}'.format(tmp * count), end='')
    print('')
