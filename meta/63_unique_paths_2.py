class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(1, n):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = dp[0][i - 1]
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i - 1][0]

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
    print(sol.uniquePathsWithObstacles([[0,1],[0,0]]))

# dp(i, j) = number of unique paths to get to (i, j).
# Recurrence relation:
# if grid(i, j) == 1 then there's no way to reach that cell, so dp(i, j) = 0
# otherwise, dp(i, j) = dp(i - 1, j) + dp(i, j - 1)
# Initialize with dp(0, 0) = 1 if it's not an obstacle
# The top row should be all 1s, unless there's an obstacle, then everything to its right including it is 0.
# The leftmost column should be all 1s, unless there's an obstacle, then everything below it including it is 0.
