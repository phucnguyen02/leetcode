class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        if n == 1: return 0
        if n == 2: return max(0, prices[1] - prices[0])
        res = 0
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                res  += (prices[i] - prices[i-1])
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))
    print(sol.maxProfit([7,6,4,3,1]))
    

# Variables: dp(i) being the maximum profit on day i.
    
# Base case: dp(0) = 0
    
# Recurrence relation:
    # dp(i) = dp(i - 1) 
    # dp(i) += prices[i] - prices[i-1] if prices[i] > prices[i-1]

# The best solution is to buy the lowest stock at a certain point and eventually sell it if it reaches its peak.
# For example, [1, 5, 9, 3, 7] means you buy the stock at 1 and sell it at 9 and then buy it at 3 again and sell it at 7.

    