class Solution:
    def jump(self, nums) -> int:
        res = 0
        l = r = 0
        while r < len(nums) - 1:
            furthest = 0

            for i in range(l, r + 1):
                furthest = max(furthest, nums[i] + i)
            
            l = r + 1
            r = furthest
            res += 1
        return res
    
# At each step, consider a window that's basically the steps we can jump to. Inside the window, find the step that jumps the furthest,
# that would be the right border of our new window. The new left border would be the previous right border + 1.
# The number of windows we create aside from the first one at 0, 0 is the number of steps we take to get to the final index