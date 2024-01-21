class Solution:
    def maxArea(self, height) -> int:
        n = len(height)
        left = 0
        right = n - 1
        max_water = -1e9
        while left < right:
            max_water = max((right - left) * min(height[left], height[right]), max_water)

            if height[left] < height[right]: left += 1
            else: right -= 1
            
        return max_water

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
    print(sol.maxArea([1,1]))



