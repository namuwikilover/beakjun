N=int(input()); l=[];
for i in range(N):
     l.append(list(map(str, input().split())))
for i in range(N):
     l[i][1]=int(l[i][1]); l[i][2]=int(l[i][2]); l[i][3]=int(l[i][3])
l=sorted(sorted(sorted(sorted(l, key=lambda x: x[1], reverse=True), key=lambda x: x[2]), key=lambda x: x[3], reverse=True), key=lambda x: x[0])
# l=sorted(l, key=lambda x: (x[2]))
# l=sorted(l, key=lambda x: (x[3]), reverse=True)
# l=sorted(l, key=lambda x: (x[0]))
print(l)
