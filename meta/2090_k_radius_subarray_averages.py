class Solution:
    def getAverages(self, nums, k: int):
        running_sum = 0
        left = 0
        n = len(nums)
        res = [-1]*n

        for right in range(n):
            running_sum += nums[right]

            if right >= 2*k:
                res[left + k] = running_sum // (2 * k + 1)
                running_sum -= nums[left]
                left += 1

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.getAverages([7,4,3,9,1,8,5,2,6], 3))
    print(sol.getAverages([100000, 100000], 0))
    print(sol.getAverages([8], 100000))

# Just simple sliding window, maintaining a window of size 2*k + 1, and updating the left + k-th index of the result