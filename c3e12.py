
print('華氏\t\t\t攝氏')
for f in range(10, 250, 10):
    c = 5 / 9 * (f - 32)
    print('{:<4}\t{:>10.2f}'.format(f, c))
