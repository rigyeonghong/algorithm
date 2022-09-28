import sys
n = int(sys.stdin.readline())

start = int(n**(1/2))

while True:
    tmp = start
    tmp_sum = start
    tmp_list = list(str(tmp))
    tmp_sum += sum(map(int,tmp_list))
    if tmp_sum == n:
        break
    # 생성자 없을 때 0
    elif tmp == n:
        start = 0
        break
    start += 1

print(start)