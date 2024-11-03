class Solution:
    def maxSubArray(self, nums) -> int:
        prev_max = nums[0]
        res = nums[0]
        for num in nums[1:]:
            prev_max = max(prev_max + num, num)
            res = max(res, prev_max)
        return res
    
# Kadane's algorithm:
# To find the maximum subarray, at each index, the max is the max between the previous max subarray + the current num, or only the num.
# We try to find the maximum subarray ending at each num, essentially