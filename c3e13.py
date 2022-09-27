
n = int(input())
count = 0

for i in range(3, (n+1), 2):
    count += ((i-2) / i)

print('total = {:.5f}'.format(count))
