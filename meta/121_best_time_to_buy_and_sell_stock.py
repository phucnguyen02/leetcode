class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        if n == 1: return 0
        if n == 2: return max(0, prices[1] - prices[0])
        dp = [[-1e9]*2 for i in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], -prices[i])
        return max(dp[-1])
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))
    print(sol.maxProfit([7,6,4,3,1]))
    

# Variables: dp(i, k) being the maximum profit on day i, k = 0 is when you sell the stock on day i, k = 1 is when you buy it.
    
# Base case: dp(0, 0) = 0, dp(0, 1) = -prices[0]
    
# Recurrence relation:
    # dp(i, 0) = max(dp(i-1, 0), dp(i-1, 1) + prices[i])
    # dp(i, 1) = max(dp(i-1, 1), -prices[i]) 

# If you choose to sell the stock, the max profit would be the max of the previous time you sold the stock and the previous time you bought the stock plus the current stock price
# Otherwise, the max profit would be the max of the previous time you bought the stock and your profit if you buy the stock now.

    