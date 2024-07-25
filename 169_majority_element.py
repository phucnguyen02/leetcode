from collections import Counter

class Solution:
    def majorityElement(self, nums) -> int:
        count = Counter(nums)
        for elem in count:
            if count[elem] > len(nums) // 2:
                return elem
        
        
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3,3,3,1,2]))

# Use a hash table to keep track of appearances of an elem in an array, find the one with a count larger than length / 2
        

