# O(N)
def solution(A):
    n = len(A)
    left_sum = [0] * n
    right_sum = [0] * n
    for i in range(1, n-2):
        left_sum[i] = max(0, left_sum[i-1]+A[i]) 
    
    for i in range(n-2, 0, -1):
        right_sum[i] = max(0, right_sum[i+1]+A[i]) 

    m = 0
    for i in range(1, n-1):
        m = max(m, left_sum[i-1] + right_sum[i+1])
    
    return m