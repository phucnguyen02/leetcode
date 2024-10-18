class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        n = len(nums)
        min_diff = 1e9
        res = 0
        for i in range(n):
            left = i + 1
            right = n - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum > target:
                    right -= 1
                elif sum < target:
                    left += 1
                else:
                    return sum
                
                diff = abs(target - sum)
                if min_diff > diff:
                    res = sum
                    min_diff = diff

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSumClosest([-1,2,1,-4], 1))
    print(sol.threeSumClosest([0,0,0], 1))