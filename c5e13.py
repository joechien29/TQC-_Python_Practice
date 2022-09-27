def isleap(x):
    if x % 400 == 0 or \
      (x % 4 == 0 and x % 100 != 0):
        print(f'{x} is a leap year')
    else:
        print(f'{x} is not a leap year')


def main():
    while True:
        year = int(input())
        if year != -9999:
            isleap(year)
        else:
            break


main()
