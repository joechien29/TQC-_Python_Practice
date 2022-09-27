import math

x1, y1 = eval(input())
x2, y2 = eval(input())
x3, y3 = eval(input())

s1 = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
s2 = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
s3 = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)

s = (s1 + s2 + s3) / 2

area_ = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))

print('The area of the triangle = {:.2f}'.format(area_))
