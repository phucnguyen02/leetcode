class Solution:
    def findMaxLength(self, nums) -> int:
        prefix_sum = {0: -1}
        sum = 0
        res = 0
        for (i, num) in enumerate(nums):
            sum += num if num else -1

            if sum in prefix_sum:
                res = max(res, i - prefix_sum[sum])
            else:
                prefix_sum[sum] = i
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaxLength([0 ,1]))
    print(sol.findMaxLength([0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0]))

# Use prefix sum, increment by 1 whenever we see a 1, decrement by 1 whenever we see a 0.
# If we see multiple prefix sums of the same value, then the subarray between those is valid