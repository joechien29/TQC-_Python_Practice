k = int(input())

count = 0
a = 2
print(f'The first {k} prime numbers are: ')
while count < k:
    isprime_ = 1
    divisor = 2
    while divisor <= a/2:
        if a % divisor == 0:
            isprime_ = 0
            break
        divisor += 1
    if isprime_ == 1:
        count += 1
        print(a, end=' ')
    a += 1
