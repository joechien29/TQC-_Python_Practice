a = int(input())
isprime_ = 1
divisor = 2
while divisor <= a/2:
    if a / divisor == 0:
        isprime_ = 0
        break
    divisor += 1
if isprime_ == 0:
    print(a, 'is not a prime number')
else:
    print(a, 'is a prime number')
