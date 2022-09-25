n = 4
board = [[2,2,2,2],[4,4,4,4],[8,8,8,8],[10,10,10,10]]
ans = 0
print("-----------------------------------------------------")
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
        print(merged_board)
    return merged_board

def rotate(board): # 반시계
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