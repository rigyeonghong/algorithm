import sys
n = int(sys.stdin.readline()) 
pair = int(sys.stdin.readline()) 
computers = [[] for _ in range(n+1)] 

for _ in range(pair):
    a, b = map(int, sys.stdin.readline().split())
    computers[a].append(b)
    computers[b].append(a)

visited = [0] * (n+1) 
cnt = 0
def bfs(v):
    global cnt
    visited[v] = 1
    for i in computers[v]:
        if visited[i] == 0:
            cnt += 1
            bfs(i)

bfs(1)
print(cnt)