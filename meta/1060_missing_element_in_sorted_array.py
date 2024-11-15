class Solution:
    def missingElement(self, nums, k: int) -> int:
        def missing(idx):
            return nums[idx] - nums[0] - idx

        if k > missing(len(nums) - 1):
            return nums[-1] + k - missing(len(nums) - 1)
            
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if missing(mid) >= k:
                right = mid
            else:
                left = mid + 1
            
        return nums[left - 1] + k - missing(left - 1)
    
# Do binary search to find the first element where the number of missing elements before it >= k. Then the missing element
# is between it and the element before it. Since this previous num has j elements before it missing, and we need to find the kth,
# add k - j to it to get the missing elem.
# Edge case: if k > missing(-1), that means the element is to the right of the array, so account for that.