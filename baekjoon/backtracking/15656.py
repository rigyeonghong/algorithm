import sys

N, M = map(int, sys.stdin.readline().split())
data = sorted(list(map(int, sys.stdin.readline().split())))

pick = []

def find(i, depth):
    if depth == M:
        print(*pick)
        return
    
    for j in range(N):
        pick.append(data[j])
        find(j, depth+1)
        pick.pop()

for i in range(N):
    pick.append(data[i])
    find(i, 1)
    pick.pop()