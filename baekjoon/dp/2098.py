import sys
N = int(sys.stdin.readline())  # 도시의 수
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 도시가 4개라면 1000(각 자리수별로 도시 표시) == 2**n
dp = [[0] * (1 << N-1) for _ in range(N)]  

def tsp(i, route):
    if dp[i][route] != 0:
        return dp[i][route]

    # 출발하는 도시를 0으로 정했기 때문에 모든 경로를 돌았을 때, 현위치(i)에서 0으로 갈 경우 추가
    if route == (1 << (N-1)) - 1:
        if graph[i][0]:             # 출발점으로 가는 경로가 있을 때
            return graph[i][0] 
        else:
            return float('inf')

    min_route = float('inf')

    for j in range(1, N):
        if not graph[i][j]:  # i에서 j로 가는 간선 비용이 없다면
            continue
        if route & (1 << j-1):  # 해당 도시를 방문했다면 
            continue
        # i -> j 간선 + j에서 다음 경로로 가는 간선
        D = graph[i][j] + tsp(j, route | (1 << (j-1)))  
        if min_route > D:
            min_route = D
    # 루트가 모든 도시를 순회할 때까지 완전탐색하기 때문에 최소값 계속 갱신
    dp[i][route] = min_route
    return min_route

print(tsp(0,0))  # 순서는 상관X 사이클의 최소비용을 구하면 되기 때문에 임의의 도시 0에서 시작
# 0은 시작점이니까 빼고 시작해야 시간 초과 안남