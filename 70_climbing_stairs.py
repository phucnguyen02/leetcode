class Solution:
    def climbStairs(self, n, k) -> int:
        dp = [0]*(n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for j in range(max(0, i - k), i):
                dp[i] += dp[j]
        
        return dp[-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(2, 2))
    print(sol.climbStairs(4, 2))
    print(sol.climbStairs(4, 3))

# Variables: dp(i) with i being the final step. dp(i) is the number of ways to get to step i

# Base case: dp(0) = dp(1) = 1 since there's only 1 way to reach steps 0 and 1.

# Recurrence relation:  dp(i) = dp(i - k) + dp(i - k + 1) + ... + dp(i - 1)

# Count all the ways to get to step i - k, i - k + 1,...



