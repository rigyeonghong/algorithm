#O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, value in enumerate(nums):
            tmp = target - value
            if tmp in hashmap:
                return [hashmap[tmp], idx]
            else:
                hashmap[value] = idx