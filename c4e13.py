a = int(input())
b = int(input())
c = int(input())

gcd = 1
k = 2
while k <= a and k <= b and k <= c:
    if a % k == 0 and b % k == 0 and c % k == 0:
        gcd = k
    k += 1
print(f'gcd({a}, {b}, {c}) = {gcd}')
