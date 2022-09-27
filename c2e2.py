d = int(input())

if d % 15 == 0:
    print(f'{d} is a multiple of 3 and 5')
elif d % 3 == 0:
    print(f'{d} is a multiple of 3 ')
elif d % 5 ==0:
    print(f'{d} is a multiple of 5')
else:
    print(f'{d} is not a multiple of 3 or 5')