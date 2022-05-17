class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

        # new_nums = sorted(nums)
        # for i in range(1, len(new_nums)):
        #     if new_nums[i] == new_nums[i-1]:
        #         return True
        # return False
        
    ## Time Limit Exceeded
        # set_nums = set(nums)
        # for num in set_nums:
        #     if nums.count(num) > 1:
        #         return True
        # return False