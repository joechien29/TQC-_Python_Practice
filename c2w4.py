s = input('Enter a hexChar character: ')

if '0' <= s <= '9':
    print(f'The decimal value is {s}')
elif s == 'a' or s == 'A':
    print('The decimal value is 10')
elif s == 'b' or s == 'B':
    print('The decimal value is 11')
elif s == 'c' or s == 'C':
    print('The decimal value is 12')
elif s == 'd' or s == 'D':
    print('The decimal value is 13')
elif s == 'e' or s == 'E':
    print('The decimal value is 14')
elif s == 'f' or s == 'F':
    print('The decimal value is 15')
else:
    print('Invalid input')
