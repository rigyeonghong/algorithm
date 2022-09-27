import sys
n = int(sys.stdin.readline())
flower= []
for _ in range(n):
    flower.append(list(map(int, sys.stdin.readline().split())))

min_cost = int(1e9)

delta =[(0,1),(-1,0),(0,-1),(1,0)]
visited = []

def check(i, j, visited):
    for d in delta:
        x = i+ d[0]
        y = j+ d[1]
        if (x, y) in visited:
            return False
    return True

def dfs(visited, cost):
    global min_cost
    if cost >= min_cost:
        return
    if len(visited) == 15:
        min_cost = min(cost, min_cost)
        return
    
    for i in range(1, n-1):
        for j in range(1, n-1):
            if check(i, j, visited) and (i,j) not in visited:
                tmp = [(i,j)]
                tmp_cost = flower[i][j]
                for d in delta:
                    dx = i + d[0]
                    dy = j + d[1]
                    tmp.append((dx,dy))
                    tmp_cost += flower[dx][dy]
                dfs(visited + tmp, cost + tmp_cost)
                
dfs(visited, 0)
print(min_cost)