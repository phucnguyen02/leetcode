class Solution:
    def getFinalState(self, nums, k: int, multiplier: int):
        for _ in range(k):
            minimum = min(nums)
            idx = 0
            for j in range(len(nums)):
                if nums[j] == minimum:
                    idx = j
                    break
            nums[idx] *= multiplier

        return nums
    
if __name__ == "__main__":
    sol = Solution()
    #print(sol.getFinalState([2,1,3,5,6], 15, 2))
    print(sol.getFinalState([4, 4, 6, 5, 6], 11, 2))