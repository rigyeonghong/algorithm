import sys
from typing import List
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
m = int(input())
dp = [[0] * (n+1) for _ in range(n+1)]

for number in range(n):
    for s in range(n-number):
        e = s + number
        if s == e :
            dp[s][e] = 1
        elif data[s] == data[e]:
            if s + 1 == e :
                dp[s][e] = 1
            elif dp[s+1][e-1] == 1:
                dp[s][e] = 1

for _ in range(m):
    start,end = map(int,input().split())
    print(dp[start-1][end-1])