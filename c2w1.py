a, b, c = eval(input('Enter a, b, c: '))

x1 = (-1 * b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
x2 = (-1 * b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

if (b ** 2 - 4 * a * c) < 0:
    print('No solution')
elif x1 == x2:
    print('The solution are {:.6f}'.format(x1))
else:
    print('The solution are {:.6f} and {:.6f}'.format(x1, x2))
