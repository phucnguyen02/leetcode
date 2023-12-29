class Solution:
    def coinChange(self, amount, coins) -> int:
        n = len(coins)
        dp = [[float('inf') for i in range(n)] for j in range(amount + 1)]
        for i in range(amount + 1):
            if i % coins[0] == 0: dp[i][0] = i // coins[0]

        for i in range(amount + 1):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1]
                if coins[j] <= i:
                    dp[i][j] = min(dp[i][j], dp[i - coins[j]][j] + 1)

        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.coinChange(11, [1, 2, 5]))
    print(sol.coinChange(3, [2]))
    print(sol.coinChange(0, [1]))
    print(sol.coinChange(2, [1, 2]))

# Same as count number of score combinations
# Variables: dp(i, j) with i being total score and j being index of scores. dp(i, j) indicates how many combinations can be made from elements all the way up to index j and sum up to i
    
# Base case: If total score i is divisible by the first element then dp(i, 0) = i / coins[0]

# Recurrence relation:
# dp(i, j) = dp(i, j - 1)
# if scores[j] <= i then dp(i, j) = min(dp(i - scores[j], j) + 1, dp(i, j))

# We compare the previous iteration with a combination that doesn't include the value of the current coin and see which is smaller. We pick the smaller one to minimize
