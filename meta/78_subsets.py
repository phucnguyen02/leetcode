class Solution:
    # def subsets(self, nums):
    #     res = []
    #     n = len(nums)
    #     def backtrack(first = 0, arr = []):
    #         if len(arr) == max_len:
    #             res.append(arr[:])
    #             return
            
    #         for i in range(first, n):
    #             arr.append(nums[i])
    #             backtrack(i + 1, arr)
    #             arr.remove(nums[i])

        
    #     for max_len in range(n+1):
    #         backtrack()
        
    #     return res
    
    def subsets(self, nums):
        res = []
        n = len(nums)
        for bitmask in range(1 << n):
            subset = []
            for i in range(n):
                if (1 << i) & bitmask: subset.append(nums[i])
            res.append(subset)
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.subsets([1, 2, 3])) 

# At each index, we have a choice of whether to include it or not in our subset.
# As such, use a bitmask to keep track of which number to include. For every bitmask from 0 to 2 ** n - 1, if the i-th bit is 1 then include nums[i]
