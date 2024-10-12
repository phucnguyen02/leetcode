from collections import defaultdict

class Solution:
    def longestOnes(self, nums, k: int) -> int:
        count = defaultdict(int)
        left = 0
        res = 0
        for right in range(len(nums)):
            count[nums[right]] += 1
            while count[0] > k:
                count[nums[left]] -= 1
                left += 1
            res = max(right - left + 1, res)

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
    print(sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))

# Sliding window where the number of 0s within it is always less than or equal to k, find max window size