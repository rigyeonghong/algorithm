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
data = []
temp_gcd = 0

for i in range(N):
    n = int(sys.stdin.readline())
    data.append(n)
    if i != 0:
        if temp_gcd == 0:
            temp_gcd = data[i] - data[i-1]
        else:
            temp_gcd = gcd(temp_gcd, data[i] - data[i-1])

span = (data[-1] - data[0]) // temp_gcd
result = span + 1 - len(data)
print(result)