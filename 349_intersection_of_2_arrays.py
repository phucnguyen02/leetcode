from collections import Counter

class Solution:
    def intersection(self, nums1, nums2):
        count = Counter(nums1)
        res = set()
        for num in nums2:
            if num in count:
                res.add(num)
        return list(res)
    

        
if __name__ == "__main__":
    sol = Solution()
    print(sol.intersection([1,2,2,1], [2,2]))

# Set up a hash map counting every unique element in the first array
# Iterate through the other array, add the element that appears in the first into a set