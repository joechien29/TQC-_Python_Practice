import math

pi = math.pi

r = eval(input())

s = 2 * r * math.sin(pi / 5)
area = (5 * s ** 2) / (4 * math.tan(pi / 5))

print('Area is {:.2f}'.format(area))
