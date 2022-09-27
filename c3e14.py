
n = int(input())
count = 0
for i in range(1, n+1):
    count += 1 / i

print('1 + 1/2 + 1/3 + 1/4 + ... 1/n = {}'.format(count))
