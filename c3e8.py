times = int(input('Enter calu times'))

for i in range(times):
    num = int(input('number'))
    tmp = num
    c = 0
    while tmp != 0:
        c += tmp % 10
        tmp //= 10
    print(f'Sum of all digits of {num} is {c}')
