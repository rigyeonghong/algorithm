import sys
from collections import deque
n, w, l = map(int, sys.stdin.readline().split()) #트럭수 / 다리길이 (que 길이) / 다리 최대 하중 (que에 한번에 들갈수 있는)
truck = list(map(int, sys.stdin.readline().split())) # 트럭의 무게들
time = 0
tmp = [0]*w
t = deque(truck)
bridge = deque(tmp)

if n == 1:
    print(w+1)
else:
    while bridge:
        bridge.popleft()
        time += 1
        if t:
            if t[0] + sum(bridge) <= l:
                bridge.append(t.popleft())
            else:
                bridge.append(0)
    print(time)