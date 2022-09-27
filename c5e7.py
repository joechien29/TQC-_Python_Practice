def compute(a):
    is_prime = 1
    divisor = 2
    while divisor <= a/2:
        if a % divisor == 0:
            is_prime = 0
        divisor += 1
    if a < 2:
        return False
    elif is_prime == 1:
        return True
    else:
        return False


d = int(input())
result = compute(d)
if result is True:
    print('Prime')
else:
    print('Not Prime')
