import random


def randnum(x):
    count = 0
    for i in range(x):
        print('{:>4}'.format(random.randint(1, 100)), end=' ')
        count += 1
        if count % 10 == 0:
            print('')


def main():
    n = int(input())
    randnum(n)


main()
