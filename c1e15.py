s = int(input('Enter monthly saving amount: '))

after_six_month = s * (1 + 0.001025) ** 6

print('After the sixth month, the account value is {:.2f}'.format(after_six_month))
