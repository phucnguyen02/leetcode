class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_ptr = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[zero_ptr], nums[i] = nums[i], nums[zero_ptr]
                zero_ptr += 1

        for i in range(zero_ptr, len(nums)):
            if nums[i] == 1:
                nums[zero_ptr], nums[i] = nums[i], nums[zero_ptr]
                zero_ptr += 1
        
# Use 2 pointers. Every time you encounter 0, move it to the first pointer and increment it. After all of the 0s have been moved to
# the beginning, do the same but with 1 instead, starting from where the first pointer left off