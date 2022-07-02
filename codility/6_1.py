#1 0%
def solution(A):
    set_A = set(A) 
    for a in set_A:
        if A.count(a) == 1:
            return a

#2 0%
def solution(A):
    set_A = set(A)
    while set_A:
        a = set_A.pop()
        if A.count(a) == 1:
            return a
        
#3 8%
from collections import Counter

def solution(A):
    counter = Counter(A) 
    min_count = 100001
    for c in counter:
        if counter[c] < min_count:
            min_count = counter[c]
            min_letter = c
    return min_letter

#4 8%
def solution(A):
    A.sort()
    result = {A[0]}
    for a in range(1,len(A)):
        if A[a] != A[a-1]:
            result.pop() 
            result.add(A[a])
    return result.pop()

#5 16% empty일 때 예외처리 하나 해줌 
def solution(A):
    N = len(A)
    if N ==0:
        return 0
    A.sort()
    result = {A[0]}
    for a in range(1,N):
        if A[a] != A[a-1]:
            result.pop() 
            result.add(A[a])
    return result.pop()

#6 문제를 잘못 이해함.. O(N)
def solution(A):
    set_A = set(A) 
    return len(set_A)