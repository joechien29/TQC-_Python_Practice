import random

r = random.randint(1, 100)

if r % 2 == 0:
    print(f'{r} is even number')
else:
    print(f'{r} is odd number')
