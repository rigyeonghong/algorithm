import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split()) # 노드 개수, 간선 개수
indegree =[0] * (n+1)
heights = [[] for _ in range(n+1)]
for _ in range(m):
    a, b =map(int, sys.stdin.readline().split()) 
    heights[a].append(b)
    indegree[b] += 1 # 진입 차수 1 증가

def topology_sort():
    result = [] # 알고리즘 수행 결과 담을 리스트
    q = deque()

    # 시작시 진입차수 0인 노드 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        p = q.popleft()
        result.append(p)

        for i in heights[p]: # 해당 원소와 연결된 노드들의 진입차수 1 빼기
            indegree[i] -= 1
            if indegree[i] == 0: # 새롭게 진입차수 0이 되는 노드를 큐에 삽입
                q.append(i)
    return result

result = topology_sort()
print(' '.join(map(str,result)))