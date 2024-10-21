class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        ptr1 = m - 1
        ptr2 = n - 1
        for i in range(m + n - 1, -1, -1):
            if ptr2 < 0: break
            if ptr1 >= 0 and nums1[ptr1] > nums2[ptr2]:
                nums1[i] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[i] = nums2[ptr2]
                ptr2 -= 1

# Use 3 pointers in this case, one to fill out/update nums1 that starts at the end of nums1, and 2 to iterate through the valid part of num1 and num2.
# p would be n spaces apart from p1, and p would never overtake p1
# If p2 < 0 then nums[p2] is larger than everything before nums[p1] at the current p1, so we break
# If p1 >= 0 and nums1[ptr1] > nums2[ptr2] then nums1[p] = nums1[p1]. p1 >= 0 is important because we might loop back to the end of nums1
# Otherwise, nums1[p] = nums2[p2] 
