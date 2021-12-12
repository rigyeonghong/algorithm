from collections import deque

def rotateArray(nums, k):
    dq = deque(nums)
    for i in range(k):
        tmp = dq.pop()
        dq.appendleft(tmp)
    # dq.rotate(k)
        
    return list(dq)

# 예를 들어, nums = [1,2,3,4,5]
# partialReverse(nums, 1, 3)
# 을 실행 할 경우, nums = [1, 4, 3, 2, 5] 가 됩니다.
def partialReverse(nums, start, end):
    for i in range(0, int((end-start)/2) + 1):
        nums[start + i], nums[end - i] = nums[end - i], nums[start + i]


def main():
    nums = [1,2,3,4,5]
   # partialReverse(nums, 1, 3) # [1, 4, 3, 2, 5] 를 반환합니다.
   
 #   print(nums)
    print(rotateArray([1,2,3,4,5,6,7,8,9], 4)) # [6,7,8,9,1,2,3,4,5] 를 반환해야 합니다.
    

if __name__ == "__main__":
    main()
