class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        N = len(arr)
        r = N - 1
        while r > 0 and arr[r] >= arr[r - 1]:
            r -= 1

        l = 0
        res = r
        while l < r:
            while r < N and arr[l] > arr[r]:
                r += 1

            res = min(res, r - l - 1)
            if arr[l] > arr[l + 1]:
                break
            l += 1
        return res 
    
# First consider that we might remove the prefix of the array, so move the right pointer to be the first element of the non-decreasing suffix.
# Initialize a left pointer and consider removing everything between it and right. We still need to maintain the fact that arr[l] > arr[r] to merge them,
# so increment r until that's true. If the element after l is less than it, break. Otherwise, increment left