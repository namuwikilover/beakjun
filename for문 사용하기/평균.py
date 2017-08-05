from functools import reduce
import decimal
number=int(input())
listS=[]
listS[:2]=input().split()
print(listS)
print(max(listS))
listS=list(map(int, listS))
for i in range(len(listS)):
    listS[i]=(listS[i]/max(listS))*100
result=reduce(lambda x,y: x+y, listS)/number
roundoff=decimal.Decimal(result)
print(round(roundoff,2))
