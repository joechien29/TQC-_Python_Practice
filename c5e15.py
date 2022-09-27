import math


def n_edge(n, g):
    area = (n * g ** 2) / (4 * math.tan(math.pi / n))
    print('area = {:.2f}'.format(area))


def main():
    n, g = eval(input())
    n_edge(n, g)


main()