import sys
sys.setrecursionlimit(10000)
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

if n == 1 :
    print(1)
elif m == 0:
    print(n)
else:
    visited = [0] * (n+1)

    def dfs(v):
        global visited
        visited[v] = 1
        for i in graph[v]:
            if not visited[i]:
                dfs(i)

    cnt = 0
    for i in range(1, n+1):
        if visited[i] == 0:
            cnt += 1
            dfs(i)
    print(cnt)