import sys
data = sys.stdin.readline().strip().split(".")
can = True

for i in range(len(data)):
    if data[i] == '':
        continue
    elif len(data[i]) % 2 == 1:
        can = False
        break
    aaaa = len(data[i]) // 4
    bb = (len(data[i]) -(aaaa * 4)) // 2
    data[i] = aaaa * 'AAAA' + bb * 'BB'

if can:
    print('.'.join(data))
else:
    print(-1)