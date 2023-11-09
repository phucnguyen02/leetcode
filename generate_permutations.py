class Solution:
    def generate_permutations(self, nums):
        if not nums: return []
        n = len(nums)
        res = []
        def backtracking(curr = [], seen = set()):
            if len(curr) == n:
                res.append(curr[:])
            for num in nums:
                if num not in seen:
                    curr.append(num)
                    seen.add(num)
                    backtracking(curr)
                    seen.remove(num)
                    curr.pop()
        backtracking()
        return res

        

if __name__ == "__main__":
    sol = Solution()
    print(sol.generate_permutations([1,2,3]))
    print(sol.generate_permutations([]))
    print(sol.generate_permutations([1,2,3,4]))

# Backtrack by selecting each element as the start of the permutation,
# then iterate through the rest of the elements of the array from the start,
# appending and removing from the permutation accordingly, provided that element isn't in the current permutation.
# Once the permutation length is equal to the original array length, append the permutation into the result.

# res = []
# backtrack(curr, seen):
#   if len(curr) == n:
#       append curr into res
#       return
#   for i = 0, ..., n-1
#       if nums[i] not in seen:
#           append nums[i] into curr, add it to seen
#           backtrack(curr, seen)
#           remove nums[i] from curr, remove it from seen
#
# backtrack([], empty set)
# 
# return res