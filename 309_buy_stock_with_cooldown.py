class Solution:
    def __init__(self):
        self.results = {}

    def maximize_profit(self, day, state, prices):
        if day < 0: return 0

        if (day, state) in self.results:
            return self.results[(day, state)]

        if day == 0:
            if state == 0: self.results[(day, state)] = -prices[0]
            else:  self.results[(day, state)] = 0

        else:
            if state == 0:
                self.results[(day, state)] = max(self.maximize_profit(day - 1, 0, prices), self.maximize_profit(day - 2, 1, prices) - prices[day])
            
            elif state == 1:
                self.results[(day, state)] = max(self.maximize_profit(day - 1, 0, prices) + prices[day], self.maximize_profit(day - 1, 1, prices))
            
        return self.results[(day, state)]

    def maxProfit(self, prices) -> int:
        n = len(prices)
        if n == 1: return 0
        dp = [[-1e9]*3 for i in range(n)]
        # buy = 0, sell = 1, rest = 2
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        dp[0][2] = 0
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])
        return max(dp[-1])

    def maxProfit2(self, prices) -> int:
        n = len(prices)
        if n == 1: return 0
        return max([self.maximize_profit(n - 1, i, prices) for i in range(2)])

    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit2([1,2,3,0,2]))
    sol.results = {}
    print(sol.maxProfit2([7,1,5,3,6,4]))
    sol.results = {}
    print(sol.maxProfit2([2,1]))
    print(sol.results)
    


# Variables: 1 for the current day, 1 for the state (buy/sell/rest)

# Base case:
#   Buy on day 0 means you end with -prices[0]
#   Sell and rest on day 0 do nothing, so you get 0

# Recurrence relation:
# dp(i, "buy") = max(dp(i - 1, "buy"), dp(i - 1, "rest") - prices[i]) You either hold from a previous buy or you buy again having rested the previous day
# dp(i, "sell") = dp(i - 1, "buy") + prices[i] You sell based on the optimal buy you have made on the previous day
# dp(i, "rest") = max(dp(i - 1, "sell"), dp(i - 1, "rest")) You maximize based on having no stock and you sold or rest in the previous day

# Result is max(dp(n - 1))

        