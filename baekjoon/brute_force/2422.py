'''
1, 2, 3, 4, 5

완전 탐색

1,2,3
1,2,4
1,2,5
1,3,4
1,3,5
1,4,5

2,3,4
2,3,5
2,4,5

3,4,5

'''

import sys

n, m = map(int, sys.stdin.readline().split())
no_shake = dict()

for j in range(1, n+1):
    no_shake[j] = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    small = a
    big = b
    if a > b:
        small = b
        big = a
    
    no_shake[small].append(big)

pick = []
total = [0]

def find(k, count):
    if count == 3:
        total[0] += 1
        return
    
    for i in range(k+1, n+1):
        flag = True
        for element in pick:
            if i in no_shake[element]:
                flag = False

        if flag:
            pick.append(i)
            find(i, count+1)
            pick.pop()

for t in range(1, n+1):
    pick.append(t)
    find(t,1)
    pick.pop()

print(total[0])
