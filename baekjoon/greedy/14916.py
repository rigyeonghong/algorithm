import sys

n = int(sys.stdin.readline())
cnt = 0
five = 0
two = 0

# n % 5가 짝수일 때,
if n % 5 % 2 ==0:
    # 5원 갯수
    five += n//5
    # 2원 갯수
    two += (n-five*5)/2
    cnt = five + two
    print(int(cnt))

# n % 5가 홀수일 때, 
else:
    five += n//5 -1
    remain = n - five*5
# 만약 5갯수를 -1 해도 나머지가 홀수라면 다시
    while(remain%2 != 0):
        five -= 1
        remain = n - five*5
        
    two += (n-five*5)/2 
    cnt = five + two
    print(int(cnt))

# 만약 거슬러줄 수 없으면 
# 11 -> 2(10) -> 1(5)

