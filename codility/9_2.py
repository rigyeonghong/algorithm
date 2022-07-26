#1 38%
def solution(A):
    interval_sum = 0
    max_sum = A[0]
    end = 0
    for start in range(len(A)):
        while end < len(A) :
            interval_sum += A[end]
            if max_sum <= interval_sum:
                max_sum = interval_sum
                end += 1
            else:
                break
        interval_sum -= A[start]

    return max_sum

# O(N)
def solution(A):
    max_sum = -1000000
    max_part_sum = 0

    for a in A:
        max_sum = max(max_sum, max_part_sum + a)
        max_part_sum = max(0, max_part_sum +a) 
    return max_sum