number=int(input())
for i in range(number):
    for j in range(number, i, -1):
        print('*', end='')
    print('')
