class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        clone = nums1.copy()
        ptr1 = ptr2 = 0
        while ptr1 < m and ptr2 < n:
            if clone[ptr1] <= nums2[ptr2]:
                nums1[ptr1 + ptr2] = clone[ptr1]
                ptr1 += 1
            else:
                nums1[ptr1 + ptr2] = nums2[ptr2]
                ptr2 += 1
        
        while ptr1 < m:
            nums1[ptr1 + ptr2] = clone[ptr1]
            ptr1 += 1

        while ptr2 < n:
            nums1[ptr1 + ptr2] = nums2[ptr2]
            ptr2 += 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.merge([1,2,3,0,0,0], 3, [2, 5, 6], 3))
    print(sol.merge([1], 1, [], 0))
    print(sol.merge([0], 0, [1], 1))

# Clone the first array
# Iterate through each array one element at a time and modify nums1 based on which element is smaller
# If one pointer runs through the entire array, iterate through the remaining array without comparisons