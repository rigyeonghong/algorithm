def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr1 = nums1[:m]
        print(arr1)
        flag_1 = 0
        flag_2 = 0
        idx = 0
        
        while flag_1 < len(arr1) and flag_2 < len(nums2):
            if arr1[flag_1] < nums2[flag_2]:
                nums1[idx] = arr1[flag_1]
                flag_1 += 1
                idx += 1
            else:
                nums1[idx] = nums2[flag_2]
                flag_2 += 1
                idx += 1
        # 남은거 처리하기
        if flag_1 == len(arr1): # 1은 다 돌고 2가 남은경우
            nums1[idx:] = nums2[flag_2:] # 2의 남은걸 넣어주기
        else: # 2가 다 돌고 1이 남은 경우
            nums1[idx:] = arr1[flag_1:] # 1이 남은걸 넣어주기
