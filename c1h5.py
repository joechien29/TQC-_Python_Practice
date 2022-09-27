import math

pi = math.pi
r, height = eval(input())

area = pi * r ** 2
volume = area * height

print('area:{:.2f}, volume:{:.2f}'.format(area, volume))
