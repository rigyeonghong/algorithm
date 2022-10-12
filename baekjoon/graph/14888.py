import sys
n = int(sys.stdin.readline()) 
A = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))

max_val = -int(1e9)
min_val = int(1e9)
def dfs(depth, total, plus, minus, mul, div):
    global max_val, min_val

    if depth == n:
        max_val = max(max_val, total)
        min_val = min(min_val, total)
        return

    if plus:
        dfs(depth+1, total+A[depth], plus-1, minus, mul, div)
    if minus:
        dfs(depth+1, total-A[depth], plus, minus-1, mul, div)
    if mul:
        dfs(depth+1, total*A[depth], plus, minus, mul-1, div)
    if div:
        dfs(depth+1, -(abs(total) // A[depth]) if total < 0 else total // A[depth], plus, minus, mul, div-1)

dfs(1, A[0], op[0], op[1], op[2], op[3])
print(max_val)
print(min_val)