for num in range(10):
    T = int(input())
    height_list = list(map(int, input().split()))
    count = 0
    length = len(height_list)
    for i in range(length):
        tempList = []
        if i == 0:
            tempList = sorted(height_list[0:3], reverse=True)
        elif i == 1:
            tempList = sorted(height_list[0:4], reverse=True)
        elif i == length-2 or i == length-1:
            tempList = sorted(height_list[i-2:length], reverse=True)
        else:
            tempList = sorted(height_list[i-2:i+3], reverse=True)
         
        if tempList[0] != height_list[i]:
            continue
        else:
            count += tempList[0]-tempList[1]
    print("#{}".format(num+1), count)
