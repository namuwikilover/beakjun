figure=input()
li=[]
for i in range(figure):
    li.append(input())
DP=[]
while True:
    i=0
    result+=li[i]
    first=li[i+1]
    second=li[i+2]
    if first>second:
        DP[i]=li[i]+first
    else:
        Dp[i]=li[i]+second
    

    i+=1
    # li[figure]
