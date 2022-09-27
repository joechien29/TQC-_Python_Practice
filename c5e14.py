def factor(x):
    x_sum = 1
    for i in range(1, x+1):
        x_sum *= i
        print(f'{i}! = {x_sum}')


def main():
    n = int(input())
    factor(n)


main()
