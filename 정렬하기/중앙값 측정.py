# 입력
n,k=map(int,input().split()); string=[]; result=[]; s=0
for i in range(n):
    string.append(int(input()))

# 부분 수열 만들기
for i in range(len(string)):
    for j in range(len(string)):
        if len(string[j:j+1+i])==3:
            result.append(string[j:j+1+i]) 

result_set = set(tuple(x) for x in result)
result=[list(x) for x in result_set]

# print(result)

for i in range(len(result)):
    s+=result[i][1]

print(s)