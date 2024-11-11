class Solution:
    def singleNumber(self, nums) -> int:
        res = 0
        for i in nums:
            res = res ^ i
        return res
        
# XOR of 2 of the same numbers = 0