# T의 길이 최대 50개고, S 최소 1개니까 2**50 만큼
import sys
S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()

def add_A(depth, x):
    x += "A"
    new_x = list(x)
    new_x.reverse()
    new_x = ''.join(new_x)
    # 뒤집은 걸 생각하는게 오래 걸림
    if x in T or new_x in T:
        return depth, x
    else:
        return depth, 0

def add_B(depth, x):
    x += "B"
    new_x = list(x)
    new_x.reverse()
    new_x = ''.join(new_x)
    return depth, new_x

len_s = len(S)
len_t = len(T)

def rec(depth, x):
    global answer
    if depth == 0:
        if x == T:
            answer = 1
            return 
        else:
            return

    depth, new_x = add_A(depth, x)
    if new_x  != 0:
        rec(depth-1, new_x)

    depth, x = add_B(depth, x)
    rec(depth-1, x)

answer =0
rec(len_t - len_s, S)
print(answer)