class Solution:
    def searchInsert(self, nums, target: int) -> int:
        l = 0
        r = len(nums)
        while l < r:
            m = (l + r) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        return l



if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert([1,3,5,6], 7))
    print(sol.searchInsert([1,3,4,5,5,7], 6))


# Find the largest index x such that nums[x] < target, result will be x + 1
