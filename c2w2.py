x, y = eval(input())

d = (x ** 2 + y ** 2) ** 0.5

if d <= 8:
    print(f'({x},{y}) is inside of the circle')
else:
    print(f'({x},{y}) is outside of the circle')
