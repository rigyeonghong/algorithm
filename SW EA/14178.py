T = int(input())
for i in range(T):
    N, D = map(int, input().split())
    Q = N // (2*D+1)
    R = N % (2*D+1)
    if R :
        result = Q+1
        print(f'#{i+1} {result}')
    else:
        result = Q
        print(f'#{i+1} {result}')