from itertools import*
input()
print(max(sum(abs(a-b)for a,b in zip(c,c[1:]))
for c in permutations(map(int,input().split()))))