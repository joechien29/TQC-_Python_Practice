x = int(input('Enter the number < 100: '))

for i in range(1, x+1):
    for j in range(1, i+1):
        print('{:>4}'.format(j * i), end='')
    print('')
