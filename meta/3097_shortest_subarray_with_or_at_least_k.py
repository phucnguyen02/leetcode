class Solution:
    def update_mask(self, mask, num, flag):
        bin_string = "{0:b}".format(num)[::-1]

        for (i, ch) in enumerate(bin_string):
            if ch == "1":
                mask[i] += flag
        
        return mask
    
    def get_value(self, mask):
        res = sum([num * (2 ** i) for (i, num) in enumerate(mask)])
        return res


    def minimumSubarrayLength(self, nums, k: int) -> int:
        if max(nums) >= k: return 1
        bitmask = [0]*32
        res = float("inf")

        left = 0
        mask_value = 0
        for right in range(len(nums)):
            bitmask = self.update_mask(bitmask, nums[right], 1)

            mask_value = self.get_value(bitmask)

            while mask_value >= k and left < len(nums):    
                if right - left + 1 > 0:
                    res = min(res, right - left + 1)
                bitmask = self.update_mask(bitmask, nums[left], -1)
                left += 1
                mask_value = self.get_value(bitmask)
        
        return res if res != float("inf") else -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumSubarrayLength([1,2,3], 2))
    print(sol.minimumSubarrayLength([2,1,8], 10))
    print(sol.minimumSubarrayLength([1, 2], 0))

# Have a bitmask array of size 32 + use sliding window. Every time we encounter a new number, update that bitmask array by incrementing the indices with 1.
# When we remove a number from the window, decrement the indices with 1. To get the value of the bitmask, only add the value of a bit if it's more than 0.
# If it's it more than 0 then it's 2 ** index.
# Only shrink the window if the mask value >= k