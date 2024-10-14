class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        start = i + 1
        end = len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

# Notice that an array in descending order would have no next permutation and would have to loop back.
# So we find 2 consecutive indices where nums[i] < nums[i + 1]. Thus, we know that every number after i is sorted in descending order.
# The most logical number to replace nums[i] would be the smallest number nums[j] such that nums[j] > nums[i], so that nums[j] would be the next number in the permutation
# We swap nums[j] with nums[i], thus maintaining the descending order. We want to minimize this array after nums[j] now, so we reverse it since it's in descending order
# and we get our next permutation
