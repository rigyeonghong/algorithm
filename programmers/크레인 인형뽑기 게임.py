def solution(board, moves):
    cnt = 0
    stack = []
    n = len(board)
    for move in moves:
        for i in range(n):
            if board[i][move-1] != 0:
                target = board[i][move-1]
                board[i][move-1] = 0
                if len(stack) == 0:
                    stack.append(target)
                else:
                    tmp = stack.pop()
                    if tmp != target:
                        stack.append(tmp)
                        stack.append(target)
                    else:
                        cnt += 2
                break
    return cnt