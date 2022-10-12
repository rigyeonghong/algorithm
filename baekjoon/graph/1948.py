import sys, heapq
from collections import deque
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
back_graph = [[] for _ in range(n+1)]
degree = [0] * (n+1)
for _ in range(m):
    s, e, t = map(int, sys.stdin.readline().split()) 
    graph[s].append((e,t))
    back_graph[e].append((s,t))
    degree[e] += 1
start, end = map(int, sys.stdin.readline().split())  

# 위상 정렬
distance = [0] * (n+1)
check = [0] * (n+1)
def topology_sort():
    global distance, check

    q = deque()
    for i in range(1, len(degree)):
        if degree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        for e, t in graph[now]:
            degree[e] -= 1
            distance[e] = max(distance[e], distance[now] + t)
            if degree[e] == 0:
                q.append(e)
    
    print(distance[end])
    #백트레킹
    cnt = 0
    q.append(end)
    while q:
        now = q.popleft()
        for e, t in back_graph[now]:
            if distance[now] - distance[e] == t:
                cnt += 1
                if check[e] == 0: # 중복 방문 제거
                    q.append(e) 
                    check[e] = 1
    print(cnt)

topology_sort()