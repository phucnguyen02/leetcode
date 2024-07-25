from collections import Counter

class Solution:
    def containsDuplicate(self, nums) -> bool:
        count = Counter(nums)
        for val in count.values():
            if val > 1: return True
        return False
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
    print(sol.containsDuplicate([1,2,3,4]))

    
# Chek if there's a frequency count larger than 1 with a hash map