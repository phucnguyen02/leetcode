class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        res = 0
        ones = 0
        for num in nums:
            if num:
                ones += 1
            else:
                ones = 0
            res = max(res, ones)
        return res
    
# Have a counter that keeps track of consecutive 1s, reset it when we reach a 0.