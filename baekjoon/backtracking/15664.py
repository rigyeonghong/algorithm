import sys

N,M=map(int, sys.stdin.readline().split())
data=list(map(int, sys.stdin.readline().split()))
check=[]

def solve(num,start,ans):
    if len(ans)==num:
        tmp=[data[i] for i in ans]
        if tmp in check:
            return
        for i in ans:
            print(data[i],end=' ')
        print()
        check.append(tmp)
        return
    
    for i in range(start+1,len(data)):
        solve(num,i,ans+[i])

data.sort()
for i in range(N):
    solve(M,i,[i])
