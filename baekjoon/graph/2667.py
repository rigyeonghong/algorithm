import sys
n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    graph.append(list(map(int, list(sys.stdin.readline().strip()))))

dx = [0,0,1,-1]
dy= [1,-1,0,0]

def dfs(x,y):
    global visited, cnt
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 1 and visited[nx][ny] == 0:
            cnt += 1
            dfs(nx,ny)
    return 1

total_cnt = 0 
ans = []
visited =[[0]* n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            cnt = 1
            tmp = dfs(i,j)
            ans.append(cnt)
            total_cnt += tmp

print(total_cnt)
ans.sort()
for a in ans:
    print(a)