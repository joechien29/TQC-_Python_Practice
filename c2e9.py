import math

x, y = eval(input())

d = math.sqrt((x - 5) ** 2 + (y - 6) ** 2)

if d <= 15:
    print('inside')
else:
    print('outside')