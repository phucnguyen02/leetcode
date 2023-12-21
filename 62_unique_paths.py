class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1: return 1
        dp = [[1]*n]*m
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePaths(3, 7))
    print(sol.uniquePaths(3, 2))

# Variables: dp(i, j) representing the number of unique paths to get to row i and column j

# Base case: all the squares from the first row and the first column only have 1 unique path, which is going straight

# Recurrence relation: dp(i, j) = dp(i - 1, j) + dp(i, j - 1) for 0 < i < m and 0 < j < n
# The number of unique paths leading to a square is equal to the total of the paths of the square above it and the square to the left

