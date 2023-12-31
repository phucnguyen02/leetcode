class Solution:
    def rob_helper(self, nums) -> int:
        n = len(nums)
        dp = [[0 for i in range(2)] for j in range(n)]
        dp[0][1] = nums[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1])
            dp[i][1] = dp[i - 1][0] + nums[i]
        return max(dp[-1])
    
    def rob(self, nums) -> int:
        if len(nums) == 1: return nums[0]
        return max(self.rob_helper(nums[1:]), self.rob_helper(nums[:-1]))

if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([2, 3, 2]))
    print(sol.rob([1, 2, 3, 1]))
    print(sol.rob([1, 2, 3]))

# Variables: dp(i, j) with i being the house index and j being rob or not. dp(i, 0) means you don't rob house i, and dp(i, 1) means you do
    
# Base case: dp(i, 0) = 0 and dp(i, 1) = nums[i]

# Recurrence relation:
# dp(i, 0) = max(dp(i - 1, 0), dp(i - 1, 1))
# dp(i, 1) = dp(i - 1, 0) + nums[i]

# If you don't steal house i, have it be the maximum value from the previous iteration
# If you do, have it add up to the value of the previous house that you didn't steal from
    
# Since house 0 and house n - 1 cannot be robbed together, the problem becomes finding the max of robbing houses 1 to n - 1 and houses 0 to n - 2

    
