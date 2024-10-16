class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        hash_sum = {0: -1}
        prefix_sum = 0
        for (i, num) in enumerate(nums):
            prefix_sum += num
            prefix_sum %= k
            if prefix_sum in hash_sum:
                if i - hash_sum[prefix_sum] >= 2:
                    return True
            
            else:
                hash_sum[prefix_sum] = i
        return False
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.checkSubarraySum([23,2,4,6,7], 6))
    print(sol.checkSubarraySum([23,2,6,4,7], 6))
    print(sol.checkSubarraySum([23,2,4,6,7], 13))

# Use prefix sum since it's a problem related to subarray sum
# For prefix sums A and B with B being further than A.
# Notice that A % k = B % k if the a subarray with sum % k = 0 is added to A, aka the subarray divides by k. We use that info to find if there exists a good subarray