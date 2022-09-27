nami_count = 0
chopper_count = 0
null_count = 0
for i in range(5):
    v = input()
    if v == '1':
        nami_count += 1
    elif v == '2':
        chopper_count += 1
    else:
        null_count += 1
    print('Total votes of No.1: Nami =  ', nami_count)
    print('Total votes of No.2: Chopper =  ', chopper_count)
    print('Total null vote =  ', null_count)
if nami_count > chopper_count:
    print('=> No.1 Nami won the election')
elif chopper_count > nami_count:
    print('=>No.2 Chopper won the election')
else:
    print('=>No one won the election')
