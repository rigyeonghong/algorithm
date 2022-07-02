def solution(rows, columns, queries):
    
    # rows x columns 행렬 만듦
    matrix = [[0] * (columns +1) for _ in range(rows+1)]
    cnt = 1
    for row in range(1, rows+1): 
        for col in range(1, columns+1):
            matrix[row][col] = cnt
            cnt +=1

    answer = []
    
    for x1, y1, x2, y2 in queries:
        keep = matrix[x1][y1]
        min_value = keep
         
        for k in range(x1, x2):
            tmp = matrix[k+1][y1]
            matrix[k][y1] = tmp
            min_value = min(min_value, tmp)
        
        for k in range(y1, y2):
            tmp = matrix[x2][k+1]
            matrix[x2][k] = tmp
            min_value = min(min_value, tmp)
        
        for k in range(x2,x1, -1):
            tmp = matrix[k-1][y2]
            matrix[k][y2] = tmp
            min_value = min(min_value, tmp)
        
        for k in range(y2, y1, -1):
            tmp = matrix[x1][k-1]
            matrix[x1][k] = tmp
            min_value = min(min_value, tmp)
        
        matrix[x1][y1+1] = keep
        answer.append(min_value)
    return answer