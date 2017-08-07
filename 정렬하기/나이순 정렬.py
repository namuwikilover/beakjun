N=int(input()); l=[]
for i in range(N): l.append(list(map(str, input().split())))
for i in range(N): l[i][0]=int(l[i][0])
index_list=list(range(N))
l=zip(index_list,l)
# l.sort(key=lambda x: (x[0]))
print(list(l))