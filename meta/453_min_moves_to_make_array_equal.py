class Solution:
    def minMoves(self, nums: List[int]) -> int:
        if min(nums) == max(nums): return 0
        minimum = min(nums)
        res = sum([num - minimum for num in nums])
        return res
    
# Instead of thinking it like increasing every number except 1, we should decrement 1 element and leave the rest the same instead.
# Thus, the min moves is the moves it takes to reduce every number to the minimum of the array