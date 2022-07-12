#1 0%
def solution(A, B):
    result = 0 
    down_value = 0
    for i in range(len(B)):
        if B[i] == 0:
            if A[i] > down_value:
                result += 1
        else:
            down_value = A[i]
    return result

#2 37%
def solution(A, B):
    # 0 up / 1 down
    result = 0
    max_value = 0
    current_arrow = 0
    for i in range(len(B)):
        if B[i] == 0:
            if current_arrow == B[i]:
                result += 1
                current_arrow = 0
            else: 
                if max_value < A[i]:
                    current_arrow = 0 
                    max_value = A[i]
        else:
            result += 1
            max_value = A[i]
            current_arrow = 1
    return result

#3 0%
def solution(A, B):
    cnt = 0
    stack = []
    for i in range(len(A)):
        size = A[i]
        direction = B[i]

    #0 up pop /  1 down append
    while stack:
        if direction == 0:
            p = stack[-1]
            if p < A[i]:
                stack.pop()
                stack.append(A[i])
        else:
            cnt += 1
            stack.append(A[i])
    else: 
        cnt +=1
        stack.append(A[i])
    
    cnt += len(stack)
    return cnt

#4
def solution(A, B):
    cnt = 0
    stack = []
    for i in range(len(A)):
        size = A[i]
        direction = B[i]

        # 0 up pop /  1 down append
        if direction == 0:
            while stack:
                if stack[-1] < size:
                    stack.pop()
                else:
                    break
                stack.append(size)
            else:
                cnt += 1

        else: 
            stack.append(size)

    cnt += len(stack)
    return cnt