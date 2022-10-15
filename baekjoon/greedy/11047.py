import sys
n, k = map(int, sys.stdin.readline().split()) # 종류, 만들 합
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))
coins.sort(reverse=True)

ans = [0] * (n+1)
for idx, coin in enumerate(coins):
    if coin <= k:
        ans[idx] = k // coin
        k = k % coin

print(sum(ans))