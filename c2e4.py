a, b = eval(input())
c = input()

ans = 0
if c == '+':
    ans = a + b
elif c == '-':
    ans = a - b
elif c == '*':
    ans = a * b
elif c == '/':
    ans = a / b
elif c == '//':
    ans = a // b
elif c == '%':
    ans = a % b

print(ans)
