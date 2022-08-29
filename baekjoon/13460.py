from collections import deque
import sys

n,m = map(int, sys.stdin.readline().split())
board = []
for i in range(n):
    board.append(list(sys.stdin.readline()))
    for j in range(m):
        if board[i][j] == 'R': # 빨간 구슬 위치
            rx, ry = i,j
        elif board[i][j] == 'B': # 파란 구슬 위치
            bx, by = i,j

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(rx,ry,bx,by):
    q = deque()
    q.append((rx,ry,bx,by))
    visited = []
    visited.append((rx,ry,bx,by))
    cnt = 0
    while q:
        for _ in range(len(q)):
            rx,ry,bx,by = q.popleft()
            if cnt > 10:
                print(-1)
                return
            if board[rx][ry] == 'O':
                print(cnt)
                return
            for i in range(4):
                nrx, nry = rx,ry
                while True:
                    nrx += dx[i]
                    nry += dy[i]
                    if board[nrx][nry] == '#':
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if board[nrx][nry] == 'O':
                        break
                nbx, nby = bx,by
                while True:
                    nbx += dx[i]
                    nby += dy[i]
                    if board[nbx][nby] == '#':
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    elif board[nbx][nby] == 'O':
                        break

                if board[nbx][nby] == 'O': # 파란구슬 먼저 들가거나, 동시에 구멍에 들가면 안되서, 이 경우는 무시
                    continue
                if nrx == nbx and nry == nby: # 두 구슬 위치 같다면
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by): # 더 많이 이동한 구슬이 더 늦게 이동한 구슬이므로 늦게 이동한 구슬 한 칸 뒤로
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if (nrx, nry, nbx, nby) not in visited: # 방문해본 적 없는 위치면, 새로 큐에 추가 후 방문 처리 
                    q.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        cnt +=1
    print(-1) # 10회 초과하지 않았지만 구멍에 들가지 못했을 때

bfs(rx,ry,bx,by)