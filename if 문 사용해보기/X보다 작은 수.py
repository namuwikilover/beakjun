n1, n2 = input().split()
li = []
li = input().split()
#print(li)

n1 = int(n1)
n2 = int(n2)

#int(li)
#print(type(li[1]))

#print(type(li[1]))

for i in range(n1) :
    li[i] = int(li[i])

#print(type(li[1]))

for i in range(n1) :
    if li[i] < n2 :
        print(li[i], end=' ')
