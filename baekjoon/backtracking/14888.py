# bfs 시간초과
import sys
from itertools import permutations
import itertools as it

n = int(sys.stdin.readline())
A = list(sys.stdin.readline().split())
cal = list(map(int, sys.stdin.readline().split()))

maximum = -1e9
minimum = 1e9

op = []
plus = (cal[0], "+")
minus = (cal[1] , "-")
mul = (cal[2] , "*")
div = (cal[3] , "//")

def oper(a):
    global op
    num, operate = a
    for _ in range(num):
        op.append(operate)
    return 

oper(plus)
oper(minus)
oper(mul)
oper(div)

per_op = list(permutations(op, sum(cal)))

for per in per_op:
    cnt = A[0]
    for p, a in zip(per, A[1:]):
        if int(cnt) < 0:
            cnt = abs(int(cnt))
            tmp = str(cnt) + p + str(a)
            cnt = -eval(tmp)
        else: 
            tmp = str(cnt) + p + str(a)
            cnt = eval(tmp)
    maximum = max(maximum, cnt)
    minimum = min(minimum, cnt)

print(maximum)
print(minimum)

# dfs
import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
cal = list(map(int, sys.stdin.readline().split()))

maximum = -1e9
minimum = 1e9

def dfs(depth, total, plus, minus, mul, div):
    global maximum, minimum
    if depth == n:
        maximum = max(maximum, total)
        minimum = min(minimum, total)
        return 
    
    if plus:
        dfs(depth+1, total + data[depth], plus -1, minus, mul, div)
    if minus:
        dfs(depth+1, total - data[depth], plus, minus -1, mul, div)
    if mul:
        dfs(depth+1, total * data[depth], plus, minus, mul-1, div)
    if div:
        dfs(depth+1, int(total / data[depth]), plus, minus, mul, div-1)


dfs(1, data[0], cal[0], cal[1], cal[2], cal[3])
print(maximum)
print(minimum)