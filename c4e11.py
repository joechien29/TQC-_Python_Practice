year1, year2 = eval(input())
count = 0
for i in range(year1, year2+1):
    if i % 400 == 0 or (i % 4 == 0 and i % 100 != 0):
        print('{:<6}'.format(i), end='')
        count += 1
        if count % 10 == 0:
            print('')
