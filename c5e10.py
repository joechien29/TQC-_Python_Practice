def compute(x):
    a = 0
    b = 1
    y = x-2
    print(a, b, end=' ')
    for i in range(y):
        c = a + b
        print(c, end=' ')
        a, b = b, c


num = int(input())
compute(num)
