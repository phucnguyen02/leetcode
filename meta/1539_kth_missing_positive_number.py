class Solution:
    def findKthPositive(self, arr, k: int) -> int:
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            missing = arr[mid] - mid - 1

            if missing >= k:
                right = mid
            else:
                left = mid + 1
        missing = arr[left] - left - 1
        if missing < k:
            return k + left + 1

        return k + left

# To do this in less than O(N), use binary search to find the lowest M such that the number of missing integers to the left of arr[M] >= k. missing[M] = arr[M] - M - 1
# If the number of missing integers to the left of a number is less than k then we need to check the right part of the array, and left otherwise.
# Once we have M, the missing integer is either between M - 1 and M or after M
# We compare the missing integers to the left of M with k. If k is larger, then it's after M.
# The formula is arr[M] + (k - missing[M - 1]) = arr[M] + (k - arr[M] + M + 1) = k + M + 1
# If k is smaller then it's before M. The formula is arr[M - 1] + (k - missing[M - 1]) = arr[M - 1] + (k - arr[M - 1] + M + 1 - 1) = k + M
