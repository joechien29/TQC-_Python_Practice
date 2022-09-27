year = int(input())

while year != -9999:
    if year % 400 == 0 \
       or (year % 4 == 0 and year % 100 != 0):
        print(f'{year} is leap year')
    else:
        print(f'{year} is not leap year')
    year = int(input())
