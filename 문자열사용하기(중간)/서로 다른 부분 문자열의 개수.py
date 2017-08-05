# enter
string=input()

# Variable init
result=[]

for i in range(len(string)):
    for j in range(len(string)):
        if len(string[j:j+1+i])==i+1:
            result.append(string[j:j+1+i])

print(len(set(result)))

