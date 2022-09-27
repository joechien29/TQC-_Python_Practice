start = int(input())
end = int(input())

if start > end:
    start, end = end, start
a = start
while a < end:
    is_prime = 1
    divisor = 2
    while divisor <= a/2:
        if a % divisor == 0:
            is_prime = 0
            break
        divisor += 1
    if is_prime == 1:
        print(a, end=' ')
    a += 1
