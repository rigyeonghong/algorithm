import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

# 꿀통이 제일 오른쪽
def honey_right():
    # 꿀벌1을 반대쪽 끝 
    bee1 = 0
    sum_data = sum(data) - data[bee1]
    sum1 = 0
    sum2 = sum_data 
    max = 0
    for i in range(1, n):
        sum1 = sum_data - data[i]
        sum2 -= data[i]
        sum1_2 = sum1 + sum2 
        if sum1_2 > max :
            max = sum1_2
    return(max)

# 꿀통 제일 왼쪽 
def honey_left():
    bee1 = n-1
    sum_data = sum(data) - data[bee1]
    sum1 = 0
    sum2 = sum_data 
    max = 0
    for j in range(n-2, -1, -1):
        sum1 = sum_data - data[j]
        sum2 -= data[j]
        sum1_2 = sum1 + sum2 
        if sum1_2 > max :
            max = sum1_2
    return(max)

# 꿀통이 두 벌 사이 
def honey_bet():
    return sum(data[1:-1]) + max(data[1:-1])

right =honey_right()
left = honey_left()
bet = honey_bet()

print(max(left, right, bet))