import sys

N, M = map(int, sys.stdin.readline().split())

pick = []

def find(i, depth):
    if depth == M:
        print(*pick)
        return
    
    for j in range(i, N+1):
        pick.append(j)
        find(j, depth+1)
        pick.pop()

for i in range(1, N+1):
    pick.append(i)
    find(i, 1)
    pick.pop()