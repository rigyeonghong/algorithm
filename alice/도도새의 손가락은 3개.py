N = int(input())

dp = [False] * (N + 1) 

dp[1] = 1
dp[2] = 2
dp[3] = 4

if N <= 3:
    print(dp[N])
else:
    i = 4
    while i <= N: 
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 123456
        i += 1
    print(dp[N])