# enter
string=input()

# Variable init
result=[]

for i in range(len(string)):
    for j in range(len(string)):
        if len(string[j:j+1+i])==i+1:
            result.append(string[j:j+1+i])

result_again=[x for x in result if result.count(x) >= 2]; count_list=[]

for i in range(len(result_again)):
    count_list.append(len(result_again[i]))

print(max(count_list))