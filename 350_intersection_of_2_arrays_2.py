from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        count1 = Counter(nums1)
        count2 = Counter(nums2)

        res = []
        for key in count2:
            if key in count1:
                res.extend([key]*min(count1[key], count2[key]))
        
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.intersect([1, 2, 2, 1], [2, 2]))
    print(sol.intersect([4, 9, 5], [9, 4, 9, 8, 4]))

# Use hash maps for both arrays. Iterate through every element in one hash map and see if it exists in the other. If so,
# append the minimum frequency into the array