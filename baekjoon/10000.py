import sys
from bisect import *
input=sys.stdin.readline
sys.setrecursionlimit(400000)

n=int(input())
circle=[]
for i in range(n):
	x,r=map(int,input().split())
	circle.append((x-r,x+r))
circle.sort(key=lambda x:(x[0],-x[1]))
cnt=0

def solve(a,b):
	global cnt
	if circle[a][1]==circle[b][1]:
		cnt +=1 
		return
	pos=bisect_left(circle,(circle[b][1],-2e9)) # 정렬된 circle에 삽입할 위치 return. 이미 있으면 기존 항목 앞 반환 
	if pos==len(circle):return
	if circle[pos][0]==circle[b][1]:
		solve(a,pos)

for i in range(n-1):
	if circle[i][0]==circle[i+1][0]:
		solve(i, i+1)
print(n+ cnt +1)