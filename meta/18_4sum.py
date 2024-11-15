class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i == 0 or nums[i] != nums[i - 1]:
                for j in range(i + 1, n):
                    if j == i + 1 or nums[j] != nums[j - 1]:
                        L = j + 1
                        R = n - 1

                        while L < R:
                            sum_nums = nums[i] + nums[j] + nums[L] + nums[R]
                            if sum_nums == target:
                                res.append((nums[i], nums[j], nums[L], nums[R]))
                                L += 1
                                R -= 1
                                while L < R and nums[L] == nums[L - 1]:
                                    L += 1
                            
                            elif sum_nums < target:
                                L += 1
                            
                            else:
                                R -= 1

        return res
    
# 3Sum with extra steps