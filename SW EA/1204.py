from collections import Counter
 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tnum = int(input())
    arr = list(map(int, input().split()))
     
    cnt = Counter(arr)
     
    answer = max(cnt, key=cnt.get)
 
    print("#{} {}".format(test_case, answer))