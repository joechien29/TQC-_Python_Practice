def compute(a, x, y):
    for i in range(y):
        for j in range(x):
            print('{:<2}'.format(a), end='')
        print('')


p1 = input()
p2 = int(input())
p3 = int(input())

compute(p1, p2, p3)
