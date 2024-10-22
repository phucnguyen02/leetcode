class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        total_length = len(nums1) + len(nums2)
        half = total_length // 2
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
            
        left, right = 0, len(nums2) - 1
        while True:
            mid = (left + right) // 2
            other = half - mid - 2
            
            two_left = nums2[mid] if mid >= 0 else -float('inf')
            two_right = nums2[mid+1] if mid + 1 < len(nums2) else float('inf')
            one_left = nums1[other] if other >= 0 else -float('inf')
            one_right = nums1[other + 1] if other + 1 < len(nums1) else float('inf')
            
            if two_left <= one_right and one_left <= two_right:
                if total_length % 2:
                    return min(two_right, one_right)
                else:
                    return (max(two_left, one_left) + min(one_right, two_right)) / 2
            elif two_left > one_right:
                right = mid - 1
            else:
                left = mid + 1
                
# We want to find the left partition of the combined sorted array.
# Do binary search on the smaller array. Find the midpoint m. Get half of the total length and subtract m from it to get a partition of the other array. Call this n
# If A[m] <= B[n + 1] and B[n] <= A[m + 1] then the subarrays form the left partition of the combined sorted array
# If A[m] > B[n + 1] then we need to push m back. Otherwise, move m forward.
# Account for edge cases when m or n are out of bounds

