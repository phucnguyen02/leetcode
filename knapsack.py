class Solution:
    def knapsack(self, capacity, values, weights) -> int:
        n = len(values)
        dp = [[0 for i in range(n + 1)] for j in range(capacity + 1)]
        for i in range(1, capacity + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i][j - 1]
                if weights[j - 1] <= i:
                    dp[i][j] = max(dp[i][j], dp[i - weights[j - 1]][j - 1] + values[j - 1])

        return dp[-1][-1]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.knapsack(4, [1, 2, 3], [4, 5, 1]))
    print(sol.knapsack(8, [2, 4, 7, 10], [1, 3, 5, 7]))


# Variables: dp(i, j) with i being the capacity and j being index of items. dp(i, j) indicates the maximum profit gained from items all the way up to index j with max capacity i
    
# Base case: dp(0, j) = 0 for all j because there's no way to include items such that their weights add up to 0.

# Recurrence relation:
# dp(i, j) = dp(i, j - 1)
# if weights[j] <= i then dp(i, j) = max(dp(i - scores[j], j - 1) + values[j], dp(i, j))

# We compare the previous iteration with a subset that doesn't include the profit of the current item and see which is larger. We pick the one with the larger profit.
