import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
miro = []

for _ in range(n):
    miro.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):

    que = deque()
    que.append((x,y))

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and miro[nx][ny] == 1:
                que.append((nx, ny))
                miro[nx][ny] = miro[x][y] + 1

    return miro[n-1][m-1]

print(bfs(0,0))