import sys

data = sys.stdin.readline().strip().split(".")
# ['XX', 'XX'] 
result = []
print(data)
for i in data:
    #4로 나눈 나머지가 0이면 몫* AAAA
    if len(i) % 4 ==0:
        result.append(len(i)//4 * 'AAAA')
        # print("here1")
        # print(result)
    elif len(i) % 4 ==2:
        result.append(len(i)//4 * 'AAAA' + len(i)%4//2 * 'BB')
        # print("here2")
        # print(result)
    else:
        print(-1)
        exit()
# print("here3")
output = ".".join(result)
print(output)
