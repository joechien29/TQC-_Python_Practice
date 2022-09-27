import math

tan_ = math.tan
pi_ = math.pi

s = abs(int((input())))
area_ = (5 * math.pow(s, 2)/(4 * tan_(pi_/5)))

print('Area = {:.4f}'.format(area_))
