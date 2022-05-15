class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = dict()
        
        for index, value in enumerate(nums):
            if target - value in data:
                return [data[target - value], index]
            else:
                data[value] = index 

    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]