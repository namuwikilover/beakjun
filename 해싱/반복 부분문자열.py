# enter
N=int(input()); string=input()

# Variable init
result=[]

for i in range(len(string)):
    for j in range(len(string)):
        if len(string[j:j+1+i])==i+1:
            result.append(string[j:j+1+i])

result_again=[value for value in result if result.count(value) >= 2]
print(max([len(value) for value in result_again]))