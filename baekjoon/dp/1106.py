import sys
c, n= map(int, sys.stdin.readline().split())   # c <= 1,000  , N <= 20
data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))
data.sort(key=lambda x: -x[1])

dp = [int(1e9)] * (c+100)
dp[0] = 0

for cost, cus in data:
    for i in range(cus, c+100):
        dp[i] = min(dp[i], dp[i-cus] + cost)
print(min(dp[c:]))