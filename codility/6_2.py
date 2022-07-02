# 1
def solution(A):
    A.sort()
    max_value = max(A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])
    return max_value