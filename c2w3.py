import random

d = random.randint(1, 100)

if d % 3 == 0 and d % 5 == 0:
    print(f"{d} is 3's and 5's multiply")
elif d % 3 == 0:
    print(f"{d} is 3's multiply")
elif d % 5 == 0:
    print(f"{d} is 5's multiply")
else:
    print(f"{d} is not 3's or 5's multiply")
