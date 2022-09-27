def compute(x, y):
    if x > y:
        x, y = y, x
    divisor = x - 1
    while True:
        if y % x == 0:
            return x
        elif x % divisor == 0 and y % divisor == 0:
            return divisor
        divisor -= 1


d1 = int(input())
d2 = int(input())
print(compute(d1, d2))
