def distance(x, y):
    dist = ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5
    print('the distance of (({}, {}), ({}, {})) = {:.2f}'.format(x[0], x[1], y[0], y[1], dist))


def main():
    x = eval(input())
    y = eval(input())
    distance(x, y)


main()
