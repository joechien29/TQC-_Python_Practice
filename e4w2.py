a = int(input('Enter a number1: '))
b = int(input('Enter a number2: '))
if a > b:
    a, b = b, a  # a < b
divisor = a - 1
while True:
    if b % a == 0:
        print('the greatest common factor is', a)
        break
    elif b % a != 0:
        if a % divisor != 0:
            divisor -= 1
        elif a % divisor == 0 and b % divisor == 0:
            print('the greatest common factor is', divisor)
            break
    else:
        divisor -= 1
