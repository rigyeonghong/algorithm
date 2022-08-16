#ref
import sys
# bfs 특 deque 사용
# deque 모듈 안쓰면 시간복잡도 박살 -> pop(0)가 O(n), popleft()가 O(1)
from collections import deque
m, n = map(int,sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
#좌표를 넣을 거라 [] 넣기
queue = deque([])
dx, dy = [-1,1,0,0],[0,0,-1,1]
#정답 담길 변수
res = 0

# queue에 처음 받은 토마토 위치 좌표 append
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append([i,j])

#bfs 함수. 한 번 들가면 다 돌고 나와서 재귀할 필요 없음
def bfs():
    while queue:
        # 첫 토마토 좌표 x,y 꺼내고
        x, y = queue.popleft()
        # 첫 토마토 사분면의 익힐 토마토 찾는다
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            #해당 좌표가 좌표 크기 넘으면 안되고, 그 좌표에 토마토가 익지 않은채로 있어야함 = 0
            if 0<= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
                # 익히고 1 더해주며 횟수세기
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append([nx,ny])

bfs()
for i in tomato:
    for j in i:
        if j == 0 :
            print(-1)
            exit(0)
    #다 익혔다면 최댓값이 정답
    res = max(res, max(i))
#처음 시작을 1로 했으니 1을 빼준다
print(res -1)            