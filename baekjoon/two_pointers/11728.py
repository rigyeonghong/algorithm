import sys

n,m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a_idx, b_idx = 0, 0
result = []

while a_idx < n and b_idx < m:
    if a[a_idx] < b[b_idx]:
        result.append(a[a_idx])
        a_idx += 1
    
    else:
        result.append(b[b_idx])
        b_idx += 1

while a_idx < n:
    result.append(a[a_idx])
    a_idx += 1

while b_idx < m:
    result.append(b[b_idx])
    b_idx += 1

print(" ".join(map(str, result)))