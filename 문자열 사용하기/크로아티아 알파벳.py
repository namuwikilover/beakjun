Croatia=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=', 'a', 'e', 'k']; c=0

# enter
string=input()

# Variable init
result=[]

for i in range(len(string)):
    for j in range(len(string)):
        if len(string[j:j+1+i])==i+1:
            result.append(string[j:j+1+i])

for i in result:
    if i in Croatia: c+=1

print(c)


