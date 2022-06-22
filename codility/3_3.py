def solution(A):
    left = 0
    right = sum(A)
    min_diff = 100000

    for i in range(len(A)-1):
        left += A[i]
        right -= A[i]
        min_diff = min(min_diff, abs(left - right))
    return min_diff