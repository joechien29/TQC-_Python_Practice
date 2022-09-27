p_count = 0
n_count = 0
m_count = 0
invalid_vote = 0
for i in range(10):
    print('1: Peter')
    print('2: Nancy')
    print('3: Mary')
    a = input('Which one do you prefer: ')
    if a == '1':
        p_count += 1
    elif a == '2':
        n_count += 1
    elif a == '3':
        m_count += 1
    else:
        invalid_vote += 1
    print(f'Peter: {p_count}, Nancy: {n_count}, Mary: {m_count}')

print(f'Peter: {p_count}, Nancy: {n_count}, Mary: {m_count}')
print(f'Invalid:', invalid_vote)
