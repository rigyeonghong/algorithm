#1 runtime over
def solution(N, A):
    result = [0] * N
    for idx, value in enumerate(A):
        if value <= N:
            result[value-1] += 1
        else:
            max_value = max(result)
            result = [max_value] * N
    return result

#2 77%
def solution(N, A):
    result = [0] * N
    max_result = 0
    for idx, value in enumerate(A):
        if value <= N:
            result[value-1] += 1
            max_result = max(max_result, result[value-1])
        else:
            result = [max_result] * N
    return result

#3 success
def solution(N, A):
    counter = [0] * N
    save_max = 0
    max_value = 0
    for idx, val in enumerate(A):
        if val <= N:
            if counter[val-1] < save_max:
                counter[val-1] = save_max
            counter[val-1] += 1
            max_value = max(counter[val-1], max_value)
        else:
            save_max = max_value
    for i in range(N):
        if counter[i] < save_max:
            counter[i] = save_max
    return counter