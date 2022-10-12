import sys
v, e = map(int, sys.stdin.readline().split())
edges = []
for _  in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c,a,b)) 
edges.sort() 

parents = [0]* (v+1)
for i in range(v+1):
    parents[i] = i

def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

total_cost = 0
for i in range(e):
    c, a, b = edges[i]
    if find_parent(parents, a) != find_parent(parents, b):
        union_parent(parents, a, b)
        total_cost += c
print(total_cost)