#1 O(N**2) 66% TIMEOUT ERROR
def solution(A):
    profit = 0
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            profit = max(profit, A[j] - A[i])
    return profit

#2 44% TIMEOUT ERROR, WRONG ANSWER
def solution(A):
    profit = 0
    min_value = min(A) 
    min_idx = A.index(min_value)
    while A:
        max_value = max(A) 
        max_idx = A.index(max_value)
        if max_value - min_value > 0 :
            if max_idx > min_idx:
                profit = max_value - min_value
                break
            else: 
                A.pop(max_idx)
    
    return profit

#3 O(N)
def solution(A):
    if len(A) < 2:
        return 0
    
    min_price = A[0]
    max_profit = 0
    for a in A:
        c = a - min_price
        if max_profit < c:
            max_profit = c
        if min_price > a:
            min_price = a

    return max_profit