save_money = int(input())
rate_year = eval(input())
month = int(input())

rate_month = rate_year / 12 / 100

print('Month   Amount')
for i in range(1, month + 1):
    money_with_rate = save_money * (1 + rate_month)
    save_money = money_with_rate
    print('  {}    {:>.2f}'.format(i, save_money))
