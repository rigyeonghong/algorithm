import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().split())
tree = Counter(map(int, sys.stdin.readline().split()))
start, end = 0, max(tree) 

while start <= end:
    mid = (start + end) // 2

    total_tree = 0
    for i,j in tree.items():
        if i > mid:
            total_tree += (i-mid)*j

    if total_tree >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)