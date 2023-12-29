class Solution:
    def score_combinations(self, total, scores):
        n = len(scores)
        dp = [[0 for i in range(n)] for j in range(total + 1)]
        for i in range(n):
            dp[0][i] = 1

        for i in range(total + 1):
            if i % scores[0] == 0: dp[i][0] = 1

        for i in range(1, total + 1):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1]
                if scores[j] <= i:
                    dp[i][j] += dp[i - scores[j]][j]

        for (i, row) in enumerate(dp):
            print(i, row)
        return dp[-1][-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.score_combinations(9, [2, 3, 7]))
    print(sol.score_combinations(5, [2, 3, 7]))

# Variables: dp(i, j) with i being total score and j being index of scores. dp(i, j) indicates how many combinations can be made from elements all the way up to index j and sum up to i
    
# Base case: if total is 0, there is only 1 possible score combination, being the empty set. If total score i is divisible by the first element then dp(i, 0) = 1

# Recurrence relation:
# dp(i, j) = dp(i, j - 1)
# if scores[j] <= i then dp(i, j) += dp(i - scores[j], j)