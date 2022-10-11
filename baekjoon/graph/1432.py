# <ref>
import sys, heapq
n = int(sys.stdin.readline()) 
data =[]
for _ in range(n):
    data.append(list(map(int, list(sys.stdin.readline().strip()))))
# 답이 여러 개일 경우, 사전순으로 제일 앞서는 것 출력
outdegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            graph[j+1].append(i+1)
            outdegree[i+1] += 1
# outdegree = [0, 1, 1, 0, 1, 1] # 간선 출발하던 점 : 간선 방향 뒤집음
# [[], [], [], [5], [2], [1, 4]] 
def topology_sort():
    global n

    q = []
    for i in range(1, n+1):
        if outdegree[i] == 0:
            heapq.heappush(q, -i)

    while q:
        now = -heapq.heappop(q)
        ans[now] = n

        for i in graph[now]:
            outdegree[i] -= 1
            if outdegree[i] == 0:
                heapq.heappush(q, -i)
        n -= 1

ans = [0] * (n+1)
topology_sort()
if ans.count(0) > 1: # 그래프의 번호를 수정할 수 없다.
    print(-1)
else:
    print(*ans[1:])
