def compute(a, b):
    count = 0
    for i in range(a, b+1):
        count += i
    return count


n1 = int(input())
n2 = int(input())

print(compute(n1, n2))
