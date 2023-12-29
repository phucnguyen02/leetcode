class Solution:
    def change(self, amount: int, coins) -> int:
        n = len(coins)
        dp = [[0 for i in range(n)] for j in range(amount + 1)]
        for i in range(n):
            dp[0][i] = 1

        for i in range(amount + 1):
            if i % coins[0] == 0: dp[i][0] = 1

        for i in range(1, amount + 1):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1]
                if coins[j] <= i:
                    dp[i][j] += dp[i - coins[j]][j]

        return dp[-1][-1]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.change(5, [1, 2, 5]))
    print(sol.change(3, [2]))
    print(sol.change(10, [10]))

# Same as count number of score combinations
# Variables: dp(i, j) with i being total score and j being index of scores. dp(i, j) indicates how many combinations can be made from elements all the way up to index j and sum up to i
    
# Base case: if total is 0, there is only 1 possible score combination, being the empty set. If total score i is divisible by the first element then dp(i, 0) = 1

# Recurrence relation:
# dp(i, j) = dp(i, j - 1)
# if scores[j] <= i then dp(i, j) += dp(i - scores[j], j)