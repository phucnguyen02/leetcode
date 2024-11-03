class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = 1e9
        prev_count = 0
        ptr = 0
        for i in range(len(nums)):
            if nums[i] == prev and prev_count == 2:
                continue
            
            if nums[i] != prev:
                prev_count = 0

            prev_count += 1
            prev = nums[i]
            nums[ptr] = nums[i]
            ptr += 1
        return ptr
    
# Have a pointer to keep track of where we're overwriting some elements in num, call it ptr. Have 2 variables to store the previous value and its count
# Iterate through the array. If the cur num == previous and the count == 2, then we skip this index
# Otherwise, increment prev_count and nums[ptr] = nums[i], and ptr += 1. This means that ptr would not count the duplicate elements after the count exceeds 2,
# so it stays behind. Reset prev_count if the curretn num != prev