class Solution:
    def find_pivot(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid
        return left
    
    def search(self, nums, target: int) -> int:
        pivot = self.find_pivot(nums)
        def binary_search(L, R, target):
            left = L
            right = R
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return -1

        left_search = binary_search(0, pivot - 1, target)
        if left_search != -1:
            return left_search
        return binary_search(pivot, len(nums) - 1, target)
    
    # def search(self, nums, target: int) -> int:
    #     n = len(nums)
    #     left, right = 0, n - 1
    #     while left <= right:
    #         mid = left + (right - left) // 2

    #         # Case 1: find target
    #         if nums[mid] == target:
    #             return mid

    #         # Case 2: subarray on mid's left is sorted
    #         elif nums[mid] >= nums[left]:
    #             if target >= nums[left] and target < nums[mid]:
    #                 right = mid - 1
    #             else:
    #                 left = mid + 1

    #         # Case 3: subarray on mid's right is sorted.
    #         else:
    #             if target <= nums[right] and target > nums[mid]:
    #                 left = mid + 1
    #             else:
    #                 right = mid - 1
    #     return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.search([4,5,6,7,8,9,10], 0))
    #print(sol.search([4,5,6,7,0,1,2], 0))

# Approach 1: Find the pivot and then do binary search in nums[:pivot] and nums[pivot:]
# The pivot is the first element that <= nums[-1]. Because if the mid element is larger than the final element, the pivot has to be in the right half.

# Approach 2: Do binary search without finding the pivot
# We first compare the middle num with the leftmost num in our subarray. If middle > left then the left array is sorted. But we still have to check if target is inbetween those.
# If not, discard the left subarray. Otherwise, keep it.
# If middle < left then the left subarray is rotated, and the right subarray is sorted. We still have to check if target is in the middle of middle and right, if not then
# discard the right subarray, otherwise keep it