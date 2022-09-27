import math

x_1 = float(input('x1 is: '))
y_1 = float(input('y1 is: '))
x_2 = float(input('x2 is: '))
y_2 = float(input('y1 is: '))

dist = math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)

print('( {} , {} )'.format(x_1, y_1))
print('( {} , {} )'.format(x_2, y_2))
print('Distance = {:.4f}'.format(dist))
