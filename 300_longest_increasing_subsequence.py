from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums) -> int:
        n = len(nums)
        dp = [1]*n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLIS([10,9,2,5,7,3,101,18]))
    print(sol.lengthOfLIS([0,1,0,3,2,3]))
    print(sol.lengthOfLIS([7,7,7,7,7,7,7]))
    print(sol.lengthOfLIS([1,3,6,7,9,4,10,5,6]))

# Variables: dp(i) being the longest increasing subsequence that ends at index i.

# Base case: dp(i) = 1, all elements' LIS is itself.

# Recurrence relation:
# dp(i) = max(dp(0), ..., dp(i - 1)) + 1 provided it's less than the element at i.

# Find an element smaller than i that has the longest increasing subsequence so far, and add i to the subsequence.

# Return the largest element in the dp.
