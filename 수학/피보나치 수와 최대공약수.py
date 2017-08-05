def findD(a, b) :
    d = 0
    tmp = a % b
    if(tmp == 0) :
        return b
    else:
        d = findD(b, tmp)
    return d;
def fibonacci(number):
    if number==1:
        return 0
    elif number==2:
        return 1
    return fibonacci(number-1)+fibonacci(number-2)
listS=[]
listS[:1]=input().split()
listS=list(map(int, listS))
number1=fibonacci(listS[0]+1)
number2=fibonacci(listS[1]+1)
print(listS)
print(findD(number1, number2)%1000000007)
#11778
