#5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]
def solution(n, arr1, arr2):
    new_arr1 = []
    new_arr2 = []

    for a, a2 in zip(arr1,arr2):
        binaryNum = format(a, 'b')
        if len(binaryNum) < n:
            while len(binaryNum) < n:
                binaryNum = '0' + binaryNum
        new_arr1.append(binaryNum)
        
        binaryNum2 = format(a2, 'b')
        if len(binaryNum2) < n:
            while len(binaryNum2) < n:
                binaryNum2 = '0' + binaryNum2
        new_arr2.append(binaryNum2)

    answer = []
    for i in range(n):
        tmp = ''
        new_str1 = new_arr1[i]
        new_str2 = new_arr2[i]
        for j in range(n):
            if new_str1[j] =='0' and new_str2[j] == '0':
                tmp += ' '
            else:
                tmp += '#'
        answer.append(tmp)
    return answer

#ref
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
