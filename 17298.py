from collections import deque

n = int(input())
inputValue = list(map(int, input().split()))

oh_big = [-1] * n
que = deque()

for i in range(n):
    while que and (que[-1][0] < inputValue[i]):
        tmp, idx = que.pop()
        oh_big[idx] = inputValue[i]
    que.append([inputValue[i],i])

print(*oh_big)

