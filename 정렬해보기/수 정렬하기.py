n = input()
n = int(n)
li = []
for i in range(n) :
    li.append(input())

li.sort()
for i in range(n):
    print(li[i])

