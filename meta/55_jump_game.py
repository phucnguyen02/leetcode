class Solution:
    def canJump(self, nums) -> bool:
        max_step = 0
        furthest = len(nums) - 1

        for (i, num) in enumerate(nums):
            if i <= max_step:
                max_jump = i + num
                if max_jump >= furthest: return True

                max_step = max(max_jump, max_step)

            else:
                return False
        return False
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.canJump([2,3,1,1,4]))
    print(sol.canJump([3,2,1,0,4]))

# Store a variable called max_step. If our current index <= max_step, then we can reach that index. Otherwise, we cannot reach any index after, including the last, so return false
# At each step, we attempt to cover as much distance as possible. If our jump >= len(nums) - 1 then we can reach the finish line from the current index.
# Otherwise, we update the max_step variable to maximize the index we can reach