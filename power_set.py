class Solution:
    def power_set(self, nums):
        if not nums: return []
        n = len(nums)
        res = []
        def backtracking(first = 0, arr = []):
            if len(arr) == max_len:
                res.append(arr[:])
                return
            for i in range(first, n):
                arr.append(nums[i])
                backtracking(i + 1, arr)
                arr.pop()

        for max_len in range(n+1):
            backtracking()
        return res

        

if __name__ == "__main__":
    sol = Solution()
    print(sol.power_set([1,2,3]))
    print(sol.power_set([1,2,3,4]))

# The max length of a subset can be anywhere from 0 to n.
# Backtrack by selecting each element as the start of the subset,
# then iterate through the rest of the elements of the array,
# appending and removing from the subset accordingly.
# Once the subset length is equal to the max subset length, append the subset into the result.

# res = []
# backtrack(first, arr):
#   if len(arr) == max_len:
#       append arr into res
#       return
#   for i = first, ..., n
#       append nums[i] into arr
#       backtrack(i + 1, arr)
#       remove nums[i] from arr
#
# for max_len = 0, ..., n:
#   backtrack(i, [])
# 
# return res