import sys
n, m = map(int, sys.stdin.readline().split()) 
heavy =[[] for _ in range(n+1)]
light = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    heavy[a].append(b)
    light[b].append(a)

def dfs(x, list):
    global cnt, visited

    visited[x] = 1
    for i in list[x]:
        if visited[i] == 0: 
            cnt += 1
            dfs(i, list)

answer = 0
mid = (n+1) // 2
for i in range(1, n+1):
    visited = [0] * (n+1)
    cnt = 0
    dfs(i, heavy)
    if cnt >= mid :
        answer += 1

    cnt = 0
    dfs(i, light)
    if cnt >= mid :
        answer += 1

print(answer)