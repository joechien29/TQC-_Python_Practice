n = int(input())

result = 0
for i in range(1, n):
    x = 1 / ((i ** 0.5) + ((i+1) ** 0.5))
    result += x

print('{:.4f}'.format(result))
