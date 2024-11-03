class Solution:
    def maxProduct(self, nums) -> int:
        max_prod = nums[0]
        min_prod = nums[0]
        res = max_prod
        for num in nums[1:]:
            max_prod, min_prod = max(num, max_prod*num, min_prod*num), min(num, min_prod*num, max_prod*num)
            res = max(max_prod, res)
        return res
    
# Similar to Kadane's algo, have 2 variables saving the maximum and minimum products
# The maximum product is the max of the current num, the previous max product * the current num, and the previous min product * the current num
# Current num: the previous product could be negative whereas the current is positive, so the current num would be the best pick
# Max product * cur num: the previous product is positive and cur is positive, so we could maximize
# Min product * cur_num: the previous product is negative and cur is negative, so we could maximize