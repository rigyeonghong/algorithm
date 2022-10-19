
import sys
n, stone_n = map(int, sys.stdin.readline().split())
stone = set()
for _ in range(stone_n):
    stone.add(int(sys.stdin.readline().rstrip()))
dp = [[int(1e9)] * (int((2*n)**0.5)+2) for _ in range(n+1)]
dp[1][0] = 0

for i in range(2, n+1):
    if i in stone:
        continue
    for v in range(1, int((2*i)**0.5)+1):
        dp[i][v] = min(dp[i-v][v-1], dp[i-v][v], dp[i-v][v+1]) + 1

ans = min(dp[n])
if ans == int(1e9):
    print(-1)
else:
    print(ans)