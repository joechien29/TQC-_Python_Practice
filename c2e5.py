c = input()

if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
    print(f'{c} is an alphabet')
elif '0' <= c <= '9':
    print(f'{c} is a number')
else:
    print(f'{c} is a symbol')
