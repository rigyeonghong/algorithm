#location = [sys.stdin.readline().strip() for i in range(N)]
#['1', '3', '7', '13']
# l = [sys.stdin.readline().split() for i in range(N)]
# [['1'], ['3'], ['7'], ['13']]

# 도로 한 편 ) 가로수 같은 간격 / 가능한 적은 수 나무 심기
# 추가되는 나무는 기존 나무들 사이에만
# output : 새로 심어야하는 가로수의 최소수

# N = 이미 심어져있는 가로수의 수
# N개의 줄에 심긴 가로수 위치

import sys
from math import gcd

N = int(sys.stdin.readline())
loc = [sys.stdin.readline().strip() for i in range(N)]
#['1', '3', '7', '13']
location = [int (i) for i in loc]
# [1, 3, 7, 13]

# 각각 뒤의 것에 앞의 것을 뺀 차! 들의 최대공약수 만큼 심어져야함!!

# dif = 이미 심어진 뒷 가로수에서 앞 가로수 사이의 거리 차이들을 비교해 최대공약수를 넣는 곳
dif = location[1] - location[0]
for i in range(1, len(location)):
    if i+1 < len(location):
        diff = location[i+1] - location[i]
        dif = gcd(diff, dif)

# 가로수들 사이의 거리는 최대공약수 dif 만큼 ! 비어있는 가로수 심어주기!
# 지금 가로수 + dif 가 다음 가로수가 아니면 심어주고 다시!
# 지금 가로수 + dif
# current = location[0]
# 1 3 7 13
def plant(location, dif):
    cnt = 0
    for i in range(N):
        current = location[i] + dif 
        if i+1 < len(location): 
            if current == location[i+1]:
                pass
            else:
                cnt, current = plus(cnt, current)
                if current == location[i+1]:
                    pass
                else:
                    while current != location[i+1]:
                        cnt, current = plus(cnt, current)
    return cnt

def plus(a, current): 
    a += 1
    current = current + dif
    return a, current

result = plant(location, dif)

print(result)
    

        