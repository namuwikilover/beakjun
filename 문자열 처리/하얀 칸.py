l=[]; c=0
for i in range(8): l.append(list(map(str, input().split())))
print(l[7][7])
# for i in range(8):
#     for j in range(8):
#         if l[i][j]=='F' and j%2==0: c+=1
# print(c)