import sys
from collections import deque
# que.appendleft() que.append() 오른쪽삽입 que.pop() 오른쪽 가져오고 삭제
# que.popleft() 왼쪽 가져오고 삭제 que.remove(item) 아이탬 찾아 삭제 

# dfs 재귀
# bfs 큐

def dfs(a):
    print(a, end=' ')
    visited[a] = 1
    for i in graph[a]:
        if not visited[i]:
            dfs(i)


def bfs(a):
    visited[a] = 1
    que = deque([a])
    while que:
        v = que.popleft()
        print(v, end=' ')
        # 줄바꿈 안되고 바로바로 출력하려고
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = 1
    

n, m, v =  map(int, sys.stdin.readline().split())
#n 정점개수 m 간선 개수 v 탐색 시작 정점 번호
graph = [[] for _ in range(n+1)]
#[[], [], [], [], []]
visited = [0] * (n+1)
#[0], [0], [0], [0], [0] n=4

# 인접한 그래프
for i in range(m):
    x,y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

#정렬해주기
for i in range(1, n+1):
    graph[i].sort()
  
dfs(v)
visited = [0] * (n+1)
print()
bfs(v)