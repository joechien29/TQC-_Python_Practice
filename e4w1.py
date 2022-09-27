d = int(input('Enter a number: '))

divisor = 2
while True:
    if d % divisor == 0:
        break
    divisor += 1

print('the smallest factor is', divisor)
