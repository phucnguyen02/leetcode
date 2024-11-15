class Solution:
    def count_set_bits(self, n):
        res = 0
        while n:
            res += 1
            n &= (n-1)
        return res

    def canSortArray(self, nums) -> bool:
        sorted_flag = True
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                sorted_flag = False
                break

        if sorted_flag: return True

        cur_count = -1
        last_max = -1
        cur_max = -1

        for i in range(len(nums)):
            count = self.count_set_bits(nums[i])
            if count != cur_count:
                last_max = cur_max
                cur_max = 0
                cur_count = count
            
            if last_max > nums[i]:
                return False
            
            cur_max = max(cur_max, nums[i])

        return True
    
# For any 2 consecutive sequences with different bit counts, if the max of the left sequence is larger than any element within
# the right, then the array can't be sorted since we can't swap the other element toward the front of the array.

# Count set bits for each element. If the number of bits is different from the current count then update the current count and updated the highest element to be the
# highest element of the last sequence of set bits. Maximize cur_max each time so we can update last_max later