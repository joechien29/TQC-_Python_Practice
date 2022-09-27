
a = int(input())
b = int(input())
count = 0
sum_a = 0
for i in range(a, b+1):
    if i % 4 == 0 or i % 9 == 0:
        count += 1
        sum_a += i
        print('{:<4}'.format(i), end='')
        if count == 10:
            print('')
print('')
print(count)
print(sum_a)
