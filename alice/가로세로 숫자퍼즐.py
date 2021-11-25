N = int(input())

data = [list(map(int, input().split())) for _ in range(N)]
maximum = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def east(x, y):
    if y + 3 > N - 1:
        return -1

    value = data[x][y] * data[x][y+1] * data[x][y+2] * data[x][y+3]
    return value

def south(x, y):
    if x + 3 > N - 1:
        return -1
    value = data[x][y] * data[x+1][y] * data[x+2][y] * data[x+3][y]
    return value

def south_east(x, y):
    if x + 3 <= N - 1 and y + 3 <= N - 1:
        value = data[x][y] * data[x+1][y+1] * data[x+2][y+2] * data[x+3][y+3]
        return value
    else:
        return -1

def south_west(x, y):
    if x + 3 <= N - 1 and y - 3 >= 0:
        value = data[x][y] * data[x+1][y-1] * data[x+2][y-2] * data[x+3][y-3]
        return value
    else:
        return -1

def search(x, y):
    global maximum
    e = east(x, y)
    s = south(x, y)
    s_e = south_east(x, y)
    s_w = south_west(x, y)

    big = max(e, s, s_e, s_w) 
    maximum = max(maximum, big)

for i in range(N):
    for j in range(N):
        search(i, j)

print(maximum)
