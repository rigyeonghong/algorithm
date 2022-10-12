import sys
from collections import deque
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b= map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
def bfs(s):
    global visited, ans
    visited[s] = 1

    q = deque()
    q.append(s)
    visited[s] = 1

    while q:
        p = q.popleft()
        for i in graph[p]:
            if visited[i] == 0:
                visited[i] = 1
                ans[i] = p
                q.append(i)

ans = [0] * (n+1)
visited = [0] * (n+1)
bfs(1)
for i in range(2,n+1):
    print(ans[i])
