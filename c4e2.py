
num = int(input())
d_min = num
while num != 9999:
    num = int(input())
    if d_min > num:
        d_min = num
print(d_min)
