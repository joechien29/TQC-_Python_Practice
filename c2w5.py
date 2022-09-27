d = int(input('Enter a number: '))

if d % 5 == 0 and d % 8 ==0:
    print(f'{d} can be divided by 5 or 8')
    print(f'{d} can be divided by 5 and 8')

elif d % 5 == 0 or d % 8 ==0:
    print(f'{d} can be divided by 5 or 8')
else:
    print(f"{d} can't be divided by 5 or 8")
