class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()

        def backtracking(index, target, arr):
            if target == 0:
                res.append(arr[:])
                return
            
            if target < 0:
                return
            
            for i in range(index, len(candidates)):
                if i != index and candidates[i] == candidates[i - 1]:
                    continue
                arr.append(candidates[i])
                backtracking(i + 1, target - candidates[i], arr)
                arr.pop()

        backtracking(0, target, [])
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum2([10,1,2,7,6,1,5], 8))
    print(sol.combinationSum2([1,2], 4))

# Do backtracking on a sorted array. Avoid duplicates with i != index and candidates[i] == candidates[i - 1], signifying the start has to be different each time