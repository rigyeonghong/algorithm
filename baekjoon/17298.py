from collections import deque
import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

oh_big = [-1] * n
stack = deque()

for i in range(n):
    while stack and (A[stack[-1]] < A[i]):
        idx = stack.pop()
        oh_big[idx] = A[i]
    stack.append(i)
    
print(*oh_big)