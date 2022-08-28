from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        L = [10**7] * len(nums)
        for i in range(len(nums)):
            lower_bound = bisect_left(L, nums[i])
            L[lower_bound] = nums[i]
        return len(L)