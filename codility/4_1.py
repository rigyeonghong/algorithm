# [1,3,2,4,2,2,2,2,2,2,5] = 10
# [1,3,2,5,2,2,2,4,5] = 7
# [1,3,2,5,2,2,2,4] = 7
# X =1 [1,2,4]
def solution(X, A):
    check = [0]* (X+1)
    sum = 0
    for idx, value in enumerate(A):
        if check[value] == 0:
            check[value] = 1
            sum += 1
            if sum == X:
                return idx
    return -1