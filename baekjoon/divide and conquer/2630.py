import sys
n = int(sys.stdin.readline()) # 2, 4, 8, 16, 32, 64, 128 중 하나 (2**k)
paper = [list(map(int, sys.stdin.readline().split()))for _ in range(n)]
white = 0
blue = 0

def divide(x,y,n):
    global white, blue
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j] :
                divide(x,y,n//2) # 좌측 위 # input값이 (2**n)이라서 2로 나누기 가능
                divide(x,y+n//2,n//2) # 우측 위
                divide(x+n//2,y,n//2) # 좌측 아래
                divide(x+n//2,y+n//2,n//2) # 우측 아래
                return
    if color == 0:
        white += 1
    else:
        blue += 1
    
divide(0,0,n)
print(white)
print(blue)