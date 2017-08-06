n,k = map(int, input().split())
dp=[[0 for value in range(n+1)] for value in range(n+1)]
for i in range(1, n+1):
    for j in range(i+1):
        if j==0 or i==j: dp[i][j]=1
        else: dp[i][j]=(dp[i-1][j-1]+dp[i-1][j])%10007
print(dp)
print(dp[n][k])