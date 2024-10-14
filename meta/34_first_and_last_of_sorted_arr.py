from bisect import bisect_left, bisect_right

class Solution:
    def find_left(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left
    
    def find_right(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left
    
    def searchRange(self, nums, target: int):
        if not nums: return [-1, -1]
        #left = bisect_left(nums, target)
        left = self.find_left(nums, target)
        right = self.find_right(nums, target)
        #right = bisect_right(nums, target)
        if left >= len(nums) or nums[left] != target: return [-1, -1]
        if right == len(nums) - 1 and nums[right] == target: return [left, right]
        if right == 0 or nums[right - 1] != target: return [-1, -1]
        return [left, right - 1]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange([5,7,7,8,8,10], 8))
    print(sol.searchRange([5,7,7,8,8,10], 6))
    print(sol.searchRange([], 0))

# Bisect left to find left insertion point. Make sure it's not at the end of the array
# Bisect right to find right insertion point because it will be after the rightmost target element. Check right - 1 and make sure it's not 0