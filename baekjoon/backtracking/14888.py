from audioop import mul
import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
cal = list(map(int, sys.stdin.readline().split()))

maximum = -1e9
minimum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    # 함수 안에서 전역 변수 값을 변경하기 위해서 global
    global maximum, minimum
    if depth == n:
        maximum = max(maximum, total)
        minimum = min(minimum, total)
        return

    if plus:
        dfs(depth+1, total + data[depth], plus -1, minus, multiply, divide)
    if minus:
        dfs(depth+1, total - data[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth+1, total * data[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth+1, int(total / data[depth]), plus, minus, multiply, divide-1) 


dfs(1, data[0], cal[0], cal[1], cal[2], cal[3])
print(maximum)
print(minimum)