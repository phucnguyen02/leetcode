class Solution:
    def permute(self, nums):
        res = []
        def backtracking(index):
            if index == len(nums):
                res.append(nums[:])
                return
            
            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                backtracking(index + 1)
                nums[i], nums[index] = nums[index], nums[i]
        backtracking(0)
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.permute([1, 2, 3]))

# Do backtracking. Starting from an index, swap the number at that index with every number after and recurse on that.