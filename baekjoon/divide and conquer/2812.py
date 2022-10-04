import sys
n, k  = map(int, sys.stdin.readline().split())
data = list(map(int, list(sys.stdin.readline().strip())))
del_k=k
answer = []

for i in range(n):
    while del_k and answer:
        if answer[-1] < data[i]:
            answer.pop()
            del_k-=1
        else:
            break
    answer.append(data[i])

print(''.join(map(str, answer[:n-k])))