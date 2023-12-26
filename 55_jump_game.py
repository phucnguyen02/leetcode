class Solution:
    def canJump(self, nums) -> bool:
        n = len(nums)
        dp = [False]*n
        dp[-1] = True
        for i in range(n - 2, -1, -1):
            jump = min(i + nums[i], n - 1)
            for j in range(i + 1, jump + 1):
                if dp[j]:
                    dp[i] = True
                    break
        return dp[0]


if __name__ == "__main__":
    sol = Solution()
    print(sol.canJump([2,3,1,1,4]))
    print(sol.canJump([3,2,1,0,4]))
    print(sol.canJump([2,0]))

# Work backwards, assume last block is reachable, check if you can reach the last block from the first block

# dp(i) determines if you can reach the last block from block i
# dp(n - 1) = true trivially
# dp(i) = true if among the possible jumps from i + 1 to i + nums[i], there is a block that can reach the last block

