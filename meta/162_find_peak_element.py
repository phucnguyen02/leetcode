class Solution:
    def bin_search(self, nums, l, r):
        m = (l + r) // 2
        if m == 0 and nums[m] > nums[m + 1]: return m
        if m == len(nums) - 1 and nums[m] > nums[ m - 1]: return m
        if nums[m - 1] < nums[m] and nums[m] > nums[m + 1]: return m
        if nums[m] < nums[m + 1]: return self.bin_search(nums, m + 1, r)
        return self.bin_search(nums, l, m - 1)
    
    def findPeakElement(self, nums) -> int:
        if len(nums) == 1: return 0
        return self.bin_search(nums, 0, len(nums) - 1)
    
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.findPeakElement([1,2,3,1]))
    print(sol.findPeakElement([1,2,1,3,5,6,4]))
    print(sol.findPeakElement([1,2]))

# Use binary search. If the middle element is in an increasing trend then a peak element has to be to the right. Otherwise, it's to the left.