num1 = int(input(''))
num2 = int(input(''))
num3 = int(input(''))
num4 = int(input(''))
num5 = int(input(''))

num_list = [num1, num2, num3, num4, num5]
sum_ = sum(num_list)
avg_ = sum_ / 5

print(num_list)
print('{:.1f}'.format(sum_))
print('{:.1f}'.format(avg_))
