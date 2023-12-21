class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        if obstacleGrid[0][0] == 1: return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m == 1 and n == 1: return 1
        dp = [[0 for i in range(n)] for j in range(m)]
        
        for i in range(n):
            if obstacleGrid[0][i] == 1: break
            dp[0][i] = 1

        for i in range(m):
            if obstacleGrid[i][0] == 1: break
            dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
    print(sol.uniquePathsWithObstacles([[0,1,0],[0,1,0],[0,0,0]]))
    print(sol.uniquePathsWithObstacles([[0,1],[0,0]]))

# Variables: dp(i, j) representing the number of unique paths to get to row i and column j

# Base case: all the squares from the first row and the first column only have 1 unique path, which is going straight. However, if the row or column has an obstacle in the middle
# of it, all the following squares would have 0 unique paths.

# Recurrence relation: dp(i, j) = dp(i - 1, j) + dp(i, j - 1) for 0 < i < m and 0 < j < n and grid[i][j] == 0
# The number of unique paths leading to a square is equal to the total of the paths of the square above it and the square to the left

