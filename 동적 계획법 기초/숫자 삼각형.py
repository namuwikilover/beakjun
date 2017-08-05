import sys

# n enter
n = int(sys.stdin.readline())

tri = [[0 for col in range(n+1)] for row in range(n+1)]
dp = [[0 for col in range(n+1)] for row in range(n+1)]

i = 1

while i <= n:
    numbers = sys.stdin.readline()
    if len(numbers) <= 1:
        tri[i][1] = int(numbers)
    else:
        num_li = numbers.split()
        k = 1
        while k <= len(num_li):
            tri[i][k] = int(num_li[k-1])
            k += 1
    i += 1

for i in range(1, n+1):
    for j in range(1, i+1):
        left = dp[i-1][j-1]
        right = dp[i-1][j]
        if left>right:
            dp[i][j] = left+tri[i][j]
        else:
            dp[i][j] = right+tri[i][j]

print(max(dp[-1]))

