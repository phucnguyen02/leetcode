class Solution:
    def threeSum(self, nums):
        res = set()
        dupes = set()
        
        for i in range(len(nums)):
            if nums[i] not in dupes:
                dupes.add(nums[i])
                hash_set = {}
                for j in range(i + 1, len(nums)):
                    target = -nums[i] - nums[j]
                    if nums[j] in hash_set:
                        res.add(tuple(sorted([nums[i], nums[j], target])))
                    hash_set[target] = nums[j]
        return res
    
    def threeSum_sort(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0: break
            if i == 0 or nums[i] != nums[i - 1]:
                L = i + 1
                R = len(nums) - 1
                
                while L < R:
                    target = nums[i] + nums[L] + nums[R]
                    if target == 0:
                        res.append((nums[i], nums[L], nums[R]))
                        L += 1
                        R -= 1
                        while L < R and nums[L] == nums[L - 1]:
                            L += 1
                    
                    elif target < 0:
                        L += 1
                    
                    else:
                        R -= 1

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum_sort([-1,0,1,2,-1,-4]))

# Approach 1: Sort the array and do 2sum 2 on the rest
# 2sum 2 relies on the array being sorted. We fix an index and do 2sum 2 on the right side of it.
# If the sum of the 3 numbers is negative, then we need to move the left pointer to increase it and vice versa.
# If the sum is 0, then we add it to the result and shrink the window
# We want to handle duplicates as well. If the first index is the same as the previous index then there's no point in processing the same thing again if we only care about the numbers
# If the left pointer is the same as the left pointer - 1 then we keep increasing it because there's no point in processing the same thing again.

# Approach 2: Fix an index and do 2sum on the rest
# Fix an index and do 2sum on the right side of it with a hash map with the target being the negative value of the first index.
# Avoid duplicates by checking if we've already seen the first index