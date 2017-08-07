N=int(input()); l=[]
for i in range(5):
    l.append(list(map(int, input().split())))
l=sorted(l, key=lambda x: (x[0], x[1]))
for i in l:
    for j in i:
        if j%2==0: print('\n')
        print(j, end=' ')