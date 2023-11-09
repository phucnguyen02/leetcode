class Solution:
    def size_k_subsets(self, nums, k):
        if not k: return [[]]
        if not nums: return []
        n = len(nums)
        res = []
        def backtracking(first = 0, arr = []):
            if len(arr) == k:
                res.append(arr[:])
                return
            for i in range(first, n):
                arr.append(nums[i])
                backtracking(i + 1, arr)
                arr.pop()

        backtracking()
        return res

        

if __name__ == "__main__":
    sol = Solution()
    print(sol.size_k_subsets([1,2,3, 4], 2))
    print(sol.size_k_subsets([1,2,3], 0))
    print(sol.size_k_subsets([], 10))

# Backtrack by selecting each element as the start of the subset,
# then iterate through the rest of the elements of the array,
# appending and removing from the subset accordingly.
# Once the subset length is equal to the max subset length, append the subset into the result.

# res = []
# backtrack(first, arr):
#   if len(arr) == k:
#       append arr into res
#       return
#   for i = first, ..., n
#       append nums[i] into arr
#       backtrack(i + 1, arr)
#       remove nums[i] from arr
#
# backtrack(0, [])
# 
# return res