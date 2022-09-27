import math

tan_ = math.tan
pi_ = math.pi

n = abs(int(input()))
s = abs(int(input()))
area_ = (n * math.pow(s, 2) / (4 * tan_( pi_ / n)))

print('Area = {:.4f}'.format(area_))
