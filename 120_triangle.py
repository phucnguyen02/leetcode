class Solution:
    def minimumTotal(self, triangle) -> int:
        n = len(triangle)
        dp = [float('inf')]*n
        dp[0] = triangle[0][0]
        for i in range(1, n):
            for j in range(len(triangle[i])):
                parent_1 = triangle[i - 1][j - 1] if 0 <= j - 1 < len(triangle[i - 1]) else float('inf')
                parent_2 = triangle[i - 1][j] if 0 <= j < len(triangle[i - 1]) else float('inf')
                triangle[i][j] += min(parent_1, parent_2)
                dp[i] = min(dp[i], triangle[i][j])

        return dp[-1]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
    print(sol.minimumTotal([[-10]]))


# Variables: dp(i) with i being the index based on the row.
# dp(i) indicates the minimum path sum up to row i
    
# Base case: dp(0) = triangle[0][0]

# Recurrence relation:
# Let parent_1 and parent_2 be the squares above the square at i, j. triangle[i][j] += min(parent_1, parent_2)
# Store minimum path value that ends at a square in itself so that the dp array is only O(n)
# dp(i) = min(dp(i), triangle[i][j])

# For any square, the minimum path total that ends on that square is equal to itself plus the minimum path total that ended on either of its parents.