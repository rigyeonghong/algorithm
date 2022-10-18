import sys
string = sys.stdin.readline().strip().split('-')
ans = 0
for s in string[0].split('+'):
    ans += int(s)
for s in string[1:]:
    for j in s.split('+'):
        ans -= int(j)
print(ans)