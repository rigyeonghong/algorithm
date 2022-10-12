import sys
sys.setrecursionlimit(10**6)
k = int(sys.stdin.readline())
for _ in range(k):
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    def bfs(i):
        global visited
        for j in graph[i]:
            if visited[j] == 0:
                visited[j] = -visited[i]
                bfs(j)
            elif visited[j] == visited[i]:
                visited[0] = 1

    visited = [0] * (v+1)
    for i in range(1,v+1):
        if visited[i] == 0:
            visited[i] = 1
            bfs(i)
    if visited[0] == 1:
        print("NO")
    else:
        print("YES")