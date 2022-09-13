n = int(input())
A = []
for m in map(int, input().split()):
    A.append(m)
B, C = map(int, input().split())

answer = [] 
cnt = 0
for a in A:
    cnt = 1
    if a - B > 0:
        if a - B - C > 0:
            cnt += int((a - B) / C)
            if (a - B) % C != 0:
                cnt += 1
        else:
            cnt += 1
    answer.append(cnt)

print(sum(answer))

#ref
print(sum(1 if a<=B else 2+(a-B-1)//C for a in A))