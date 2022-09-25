import sys

min_cost= 1e9
n = int(sys.stdin.readline())
cost = []
for _ in range(n):
    cost.append(list(map(int, sys.stdin.readline().split())))

def circuit(depth, node, visited, total):
    
    global min_cost
    if depth == n:
        # 마지막에 0으로 돌아오는 값 추가 (i,0) 후 min 비교
        if cost[node][0]:
            total += cost[node][0]
            min_cost= min(min_cost, total)
            total -= cost[node][0]
            return
        return

    for i in range(n):
        if cost[node][i]:
            if visited[i] == False:
                total += cost[node][i]
                visited[i] = True
                circuit(depth+1, i, visited, total)
                visited[i] = False
                total -= cost[node][i]

total = 0
visited =[False]* n 
visited[0] = True
circuit(1, 0, visited, total)
print(min_cost)

# feat. 기운
# 하나의 root로 생기는 경우의 수 각각의 비용 중 min