d = int(input())

tmp = d
rate = 0.03
count = 0
while d < 2 * tmp:
    d = d * (1 + rate)
    count += 1
    print('#{} year:{:.2f}'.format(count, d))
print('Tuition will be double in {} year'.format(count))
