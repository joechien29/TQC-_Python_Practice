x = int(input())
y = int(input())

sum_even = 0
for i in range(x, y+1):
    if i % 2 == 0:
        sum_even += i

print(sum_even)
