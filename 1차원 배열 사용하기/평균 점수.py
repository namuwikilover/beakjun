from functools import reduce
listS=[]
for i in range(5):
    listS.append(input())
int_listS=list(map(int, listS))
for i in range(5):
    if int_listS[i]<40:
        int_listS[i]=40
print(int(reduce(lambda x,y: x+y, int_listS)/5))
