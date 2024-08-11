from collections import defaultdict

class Solution:
    def findMaxLength(self, nums) -> int:
        check = 0
        counter = defaultdict(int)
        counter[0] = -1
        res = 0
        for (i, num) in enumerate(nums):
            check += 1 if num else -1
            if check in counter:
                res = max(res, i - counter[check])
            else:
                counter[check] = i
        
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaxLength([0, 1]))
    print(sol.findMaxLength([0, 1, 0]))
    print(sol.findMaxLength([1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1]))

# Keep a counter running. Every time the counter hits 0, that means the number of 0s and 1s from the start of the array are equal.
# If the counter appears more than once in a hash table, that means the number of 0s and 1s from the index corresponding to the counter and the current index are equal.

