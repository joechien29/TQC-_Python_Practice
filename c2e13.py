a, b, c = eval(input('Enter a, b, c: '))
d, e, f = eval(input('Enter d, e, f: '))

if a * e - b * d == 0:
    print('無解')

elif a * e - b * d != 0:
    x = (c * e - b * f) / (a * e - b * d)
    y = (a * f - c * d) / (a * e - b * d)
    print(f'x is {x}, y is {y}')
