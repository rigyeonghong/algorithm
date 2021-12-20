def quickSort(array):
    if len(array) <= 1:
        return array
        
    less_values = []
    more_values = []
    pivot = array[0]
    
    for i in range(1, len(array)):
        if array[i] > pivot:
            more_values.append(array[i])
        else:
            less_values.append(array[i])
    return quickSort(less_values) + [pivot] + quickSort(more_values)
            # 2 3 4 5 6 9 7 8 2
    

def main():
    line = [int(x) for x in input().split()] # input 받은 것을 쪼개서 하나씩 line 에 넣기 # 10,2,3,4,5,6,9,7,8,1

    print(*quickSort(line))

if __name__ == "__main__":
    main()
