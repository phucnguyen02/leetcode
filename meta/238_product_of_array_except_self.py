class Solution:
    def productExceptSelf(self, nums):
        res = [1 for i in range(len(nums))]
        prefix_prod = 1
        for i in range(len(nums)):
            res[i] = prefix_prod
            prefix_prod *= nums[i]

        suffix_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix_prod
            suffix_prod *= nums[i]

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([1,2,3,4]))
    print(sol.productExceptSelf([-1,1,0,-3,3]))

# The product except self is the product of the prefix product before it and the suffix product after it
# In order to save space, we first iterate through the array to calculate the prefix product of the numbers before the number we're at.
# Similarly, we iterate through the array backwards to get the suffix product, and multiply it with the prefix product we were already storing in the results array