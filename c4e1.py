min_num = int(input('請輸入第1個數字: '))
for i in range(2, 11):
    a = int(input('請輸入第{}個數字: '.format(i)))
    if min_num > a:
        min_num = a
print(min_num)
