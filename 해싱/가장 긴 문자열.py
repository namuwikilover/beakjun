# enter
N=int(input()); string=input()

# Variable init
result=[]

for i in range(len(string)):
    for j in range(len(string)):
        if len(string[j:j+1+i])==i+1:
            result.append(string[j:j+1+i])

result_again=[x for x in result if result.count(x) >= 2]; count_list=[]
del result[:]

print(len(result_again[-1]))