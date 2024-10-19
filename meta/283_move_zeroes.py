class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr1 = ptr2 = 0
        while ptr2 < len(nums):
            if nums[ptr2] != 0:
                nums[ptr2], nums[ptr1] = nums[ptr1], nums[ptr2]
                ptr1 += 1
            ptr2 += 1

# Use 2 pointers. Every time you encounter a nonzero element, move it to the first pointer and increment it.