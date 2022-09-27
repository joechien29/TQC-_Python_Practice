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


x, y = eval(input())
m, n = eval(input())
a = x * n + m * y
b = y * n
gcd = compute(a, b)
c = int(a / gcd)
d = int(b / gcd)
print(f'{x}/{y} + {m}/{n} = {c}/{d}')
