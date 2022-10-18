import sys
from collections import deque
n = int(sys.stdin.readline())
meeting = []
for _ in range(n):
    meeting.append(list(map(int, sys.stdin.readline().split())))
meeting.sort(key=lambda x: (x[0], x[1]))

q = deque()
for s,e in meeting:
    if len(q) == 0:
        q.append([s,e])
    else:
        if q[-1][1] <= s:
            q.append([s,e])
        elif q[-1][1] > e:
            q.pop()
            q.append([s,e])
        elif q[-1][1] < e and q[-1][0] <= s < q[-1][1]:
            continue
print(len(q))