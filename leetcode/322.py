class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
# Bottom up DP (Tabulation)
        dp = [math.inf] * (amount+1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin, amount+1):
                if i-coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)
                
        return -1 if dp[-1]== math.inf else dp[-1]
        
        
# Top down DP (Memoization) 
#         def result(amount, cache):
#             if amount < 0:
#                 return math.inf
        
#             if amount == 0:
#                 return 0
        
#             if amount in cache:
#                 return cache[amount]
            
#             cache[amount] = min(result(amount-coin, cache) + 1 for coin in coins)
#             return cache[amount]
    
#         answer = result(amount, {})
#         return -1 if answer == math.inf else answer