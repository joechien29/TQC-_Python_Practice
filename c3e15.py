n = int(input())
count = 0
for i in range(n, 0, -1):
    count += 1/i

print('1/n + 1/(n-1) + 1/(n-2) + ... + 1 = {}'.format(count))
