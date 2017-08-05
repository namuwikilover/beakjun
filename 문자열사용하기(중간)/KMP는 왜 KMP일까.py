string=input()
string=string.split('-')
KMP=[]
for i in range(len(string)):
    KMP.append(string[i][0])
print(''.join(KMP))
