even_count = 0
odd_count = 0
for i in range(10):
    d = int(input())
    if d % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f'Even numbers: {even_count}')
print(f'Odd numbers: {odd_count}')
