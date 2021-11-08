
N = int(input())

Do = [input().split() for i in range(N)]
# [['push', '1'], ['push', '2'], ['front'], ['back'], ['size'], ['empty'], ['pop'], ['pop'], ['pop'], ['size'], ['empty'], ['pop'], ['push', '3'], ['empty'], ['front']]

que = []

# [['push', '1']
for i in Do:
    if i[0] == 'push':
        que.insert(0, i[1])
    elif i[0] == 'front':
        if len(que) == 0: 
            print(-1)
        else:
            print(que[len(que)-1])
    elif i[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif i[0] == 'size':
        print(len(que))
    elif i[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(que) != 0:
            print(que.pop())
        else: 
            print(-1)

    
