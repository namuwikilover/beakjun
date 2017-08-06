N=int(input())
l=[[0 for value in range(5)] for value in range(5)]
for i in range(N):
    l[i]=list(map(int, input().split()));

for i in range(N):
    e=l[i][0]
    avg=sum(l[i][-e:])/l[i][0] # 평균