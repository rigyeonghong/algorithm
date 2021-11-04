from collections import deque

n = int(input())
inputValue = list(map(int, input().split()))

oh_big = [-1] * n
stack = deque()

for i in range(n):
    while stack and (stack[-1][0] < inputValue[i]):
        tmp, idx = stack.pop()
        oh_big[idx] = inputValue[i]
    stack.append([inputValue[i],i])

print(*oh_big)

