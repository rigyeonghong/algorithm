import sys
data = sys.stdin.readline().strip().split(".")
result = []

for i in data:
    #4로 나눈 나머지가 0이면 몫* AAAA
    if len(i) % 4 ==0:
        result.append(len(i)//4 * 'AAAA')
    elif len(i) % 4 ==2:
        result.append(len(i)//4 * 'AAAA' + len(i)%4//2 * 'BB')
    else:
        print(-1)
        exit()

output = ".".join(result)
print(output)
