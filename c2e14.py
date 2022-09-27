d = input()

d_list = list(d)
if d_list[0] == d_list[-1]:
    print(f'{d} is a palindrome number')
else:
    print(f'{d} is not a palindrome number')
