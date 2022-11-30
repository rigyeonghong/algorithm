import sys
a, b = map(int, sys.stdin.readline().split())

ans = 1e9
def rec(x, cnt):
    global ans
    if x*2 == b:
        ans = min(ans, cnt+1)
    elif x*2 < b:
        rec(x*2, cnt+1)
        
    if int(str(x) + str(1)) == b:
        ans = min(ans, cnt+1)
    elif int(str(x) + str(1)) < b:
        rec(int(str(x) + str(1)), cnt+1)

rec(a, 0)
if ans == 1e9: print(-1)
else: print(ans+1)