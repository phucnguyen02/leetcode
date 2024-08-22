from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        dict = defaultdict(int)

        for (i, num) in enumerate(nums):
            if num in dict and i - dict[num] <= k: return True
            dict[num] = i
            
        return False
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.containsNearbyDuplicate([1,2,3,1], 3))
    print(sol.containsNearbyDuplicate([1, 0, 1, 1], 1))
    print(sol.containsNearbyDuplicate([1,2,3,1,2,3], 2))

# Use a hash map to store an element's last index. When it appears again, compare the current index to the stored index.