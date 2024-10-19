class Solution:
    def trap_dp(self, height):
        if not height: return 0
        n = len(height)
        left_max = [-1e9]*n
        right_max = [-1e9]*n
        left_max[0] = height[0]
        right_max[-1] = height[-1]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i - 1])
            right_max[-i - 1] = max(right_max[-i], height[-i])
        
        res = 0
        for i in range(1, n):
            res += max(0, min(left_max[i], right_max[i]) - height[i])
        
        return res
    

    def trap(self, height) -> int:
        if not height: return 0
        left_max = height[0]
        right_max = height[-1]
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            
            if left_max <= right_max:
                left += 1
                left_max = max(left_max, height[left])
                res += max(0, left_max - height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
                res += max(0, right_max - height[right])
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.trap_dp([0,1,0,2,1,0,1,3,2,1,2,1]))
    #print(sol.trap([7, 0, 3, 0, 5, 0, 6]))

# From the figure in dynamic programming approach, notice that as long as right_max[i]>left_max[i] (from element 0 to 6), the water trapped depends upon the left_max, 
# and similar is the case when left_max[i]>right_max[i] (from element 8 to 11).
# So, we can say that if there is a larger bar at one end (say right), we are assured that the water trapped would be dependant on height of bar in current direction 
# (from left to right). As soon as we find the bar at other end (right) is smaller, we start iterating in opposite direction (from right to left).
# We must maintain left_max and right_max during the iteration, but now we can do it in one iteration using 2 pointers, switching between the two.