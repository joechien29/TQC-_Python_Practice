import math

pi = math.pi

radius_c = float(input('Radius is: '))
perimeter_c = 2 * radius_c * pi
area_c = radius_c ** 2 * pi

print('Radius = {:.2f}'.format(radius_c))
print('Perimeter = {:.2f}'.format(perimeter_c))
print('Area = {:.2f}'.format(area_c))