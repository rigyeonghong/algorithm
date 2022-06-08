import sys
n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

start, end = 1, max(tree) 

while start <= end:
    mid = (start + end) // 2

    total_tree = 0
    for t in tree:
        if t >= mid:
            total_tree += t - mid

    if total_tree >= m:
        start = mid + 1
    else:
        end = mid - 1
    
print(end)