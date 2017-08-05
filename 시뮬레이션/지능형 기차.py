li = []
li2 = []

for i in range(8):
    li.append(input().split(','))

li = list(map(int, li))

for i in range(8):
    if i%2==1:
        sum += li[i]
    else:
        sum -= li[i] 

    if i%2==1:
        li2 = sum

print(li2)
