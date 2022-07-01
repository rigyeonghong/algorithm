# 내가 오른쪽으로 가려하는데 나보다 오른쪽에 있는애가 왼쪽으로 오는 갯수
# Count는 O(N)
#1 70% wrong answer : 예외처리 잊음
def solution(A):
    # 왼쪽으로 오는 애들 수
    count= 0
    west_count = A.count(1)
    for i in range(len(A)):
        if A[i] == 0:
            count += west_count
        else:
            west_count -= 1 
    return count

#2 O(N)
def solution(A):
    # 왼쪽으로 오는 애들 수
    count= 0
    west_count = A.count(1)
    for i in range(len(A)):
        if A[i] == 0:
            count += west_count
        else:
            west_count -= 1 
    if count > 1000000000: 
        return -1
    return count