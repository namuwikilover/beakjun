line=input()
for i, str in enumerate(line):
    if i%10==0 and i!=0:
        print('')
    print(str, end='')
