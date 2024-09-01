class Solution:
    def maxFrequency(self, nums, k: int) -> int:
        nums.sort()
        left = 0
        res = 0
        curr_sum = 0

        for right in range(len(nums)):
            target = nums[right]
            curr_sum += target

            while (right - left + 1) * target - curr_sum > k:
                curr_sum -= nums[left]
                left += 1
            
            res = max(res, right - left + 1)
        
        return res



if __name__ == "__main__":
    sol = Solution()
    print(sol.maxFrequency([1, 2, 4], 5))
    print(sol.maxFrequency([1, 4, 8, 13], 5))


# The target element is within the array
# For each element, create a sliding window for the elements before it to see if it's possible to
# raise all of the elements in that window to be equal to the last element.
# In other words, if the sum of that window after the raise subtracted by the sum of that window before the raise is less than
# or equal to k, it's possbile to raise every element. The frequency of the target would be equal to the valid window's size.

# curr_sum = left = res = 0
# for right = 0, ..., len(nums) - 1
#   curr_sum += nums[right]
    # while window_size * target - curr_sum > k then
    #     curr_sum -= nums[left]
    #     left += 1

    # res = max(res, window_size)
# return res