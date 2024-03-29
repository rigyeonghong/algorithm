import sys

N = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, i+1):
        if j == 1:
            dp[i][j] = dp[i-1][j] + data[i-1][j-1]        
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + data[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + data[i-1][j-1]

print(max(dp[N]))