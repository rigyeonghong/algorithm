# 1 75% O(N***3) TIMEOUT ERROR
from itertools import combinations

def solution(A):
    com = combinations(A,3)

    for c in com:
        if c[0]+ c[1] > c[2] and c[1]+ c[2] > c[0] and c[0]+ c[2] > c[1]:
            return 1
    return 0

#2
def solution(A):
    A.sort()
result = 0
for i in range(len(A)-2):
    if A[i] + A[i+1] > A[i+2]: 
        if A[i] + A[i+2] > A[i+1]:
            if A[i+2] + A[i+1] > A[i]:
                result = 1
return result