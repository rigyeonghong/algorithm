import sys
n = int(sys.stdin.readline())

col = [0] * n

def is_promising(x):
    for i in range(x):
        if col[x] == col[i] or abs(col[x]-col[i]) == abs(x-i):
            return False
    return True

def queen(x):
    global cnt 
    if x == n:
        cnt += 1
        return

    for i in range(n):
        col[x] = i
        if is_promising(x):
            queen(x+1)

cnt = 0 
queen(0)
print(cnt)