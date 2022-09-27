def compute(a, b, c):
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print('Your equation has no root')
    elif delta == 0:
        print(-b / (2 * a))
    else:
        res1 = (-b + delta ** 2) / (2 * a)
        res2 = (-b - delta ** 2) / (2 * a)
        print(res1, res2)


a = eval(input())
b = eval(input())
c = eval(input())
compute(a, b, c)

