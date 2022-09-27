def multiply99():
    for i in range(1, 10):
        for j in range(1, 10):
            print('{}*{}={:>2}'.format(j, i, j*i), end='  ')
        print('')


def print_star(n):
    print('*' * n)


print_star(72)
multiply99()
print_star(72)
