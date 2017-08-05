l=list(map(int, input().split())); order=[]; cnt=0; dcnt=0;
for i in range(len(l)):
    if l[i]==i+1: cnt+=1
    elif l[i]==8-i: dcnt+=1

if cnt==8: print('ascending')
elif dcnt==8: print('descending')
elif cnt!=8 and dcnt!=8: print('mixed')
