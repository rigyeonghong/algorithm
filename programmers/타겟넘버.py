# numbers 안의 수를 더하거나, 빼서 target 만드는 방법 수 return
# 깊이는 Numbers의 len
from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append([numbers[0],0])
    queue.append([-1*numbers[0],0])
    
    while queue:
        node, idx = queue.popleft()
        idx += 1
        if idx < len(numbers):
            queue.append([node+numbers[idx], idx])
            queue.append([node-numbers[idx], idx])
        else:
            if node == target:
                answer += 1
    return answer
            
    
