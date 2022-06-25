def solution(A):
    if max(A) != len(A) or len(set(A)) != len(A):
        return 0
    return 1