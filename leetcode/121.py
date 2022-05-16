class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, benefit = float('inf'), 0

        for p in prices:
            buy, benefit = min(buy, p), max(benefit, p-buy)

        return benefit

'''   
mini = 100000000
max_benefit = 0

for i in prices:
    mini = min(mini, i)
    
    if i - mini > 0:
        max_benefit = max(max_benefit,i - mini)
    
return max_benefit
'''