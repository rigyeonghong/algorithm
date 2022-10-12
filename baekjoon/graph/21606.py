import sys
from collections import deque
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
A =list(map(int, list(sys.stdin.readline().strip())))
graph = [[] for _ in range(n+1)]
ans = 0
for _ in range(n-1):
    v, e = map(int, sys.stdin.readline().split())
    graph[v].append(e)
    graph[e].append(v)
    if A[v-1] == 1 and A[e-1] == 1:
        ans += 2

def dfs(i,cnt):
    visited[i] = 1

    for j in graph[i]:
        if A[j-1] == 1: #실내면
            cnt +=1
        elif visited[j] == 0 and A[j-1] == 0: # 방문 안한 실외이면
            cnt = dfs(j, cnt) 
    return cnt

visited = [0] * (n+1)
for i in range(1,n+1):
    if visited[i] == 0 and A[i-1] == 0: #방문 안한 실외이면
        tmp = dfs(i,0)
        ans += tmp * (tmp-1)
print(ans)