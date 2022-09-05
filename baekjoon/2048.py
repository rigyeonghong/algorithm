n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def merge(board):
    merged_board = []
    for i in range(n):
        tmp = [j for j in board[i] if j != 0]
        for j in range(len(tmp)-1):
            if tmp[j] == tmp[j+1]:
                tmp[j] *= 2
                tmp[j+1] = 0
        tmp = [j for j in tmp if j != 0]
        merged_board.append(tmp + [0]*(n-len(tmp)))
    return merged_board

def rotate(board):
    return list(map(list, zip(*board[::-1])))

def dfs(cur_board, depth):
    if depth == 5:
        global ans
        ans = max(ans, max(map(max,cur_board)))
        return
    for _ in range(4):
        merged_board = merge(cur_board) 
        dfs(merged_board, depth+1)
        cur_board = rotate(cur_board)

dfs(board, 0)
print(ans)