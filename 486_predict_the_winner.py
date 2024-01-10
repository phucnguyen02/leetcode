class Solution:
    def choose_helper(self, nums, left, right, start):
        res = start
        cur_turn = -1

        while left < right:
            max_elem = max(nums[right], nums[left])
            
            if nums[left] < nums[right]:
                right -= 1

            else:
                left += 1
            
            max_elem *= cur_turn
            res += max_elem
            
            cur_turn *= -1

        return res
    
    def predictTheWinner(self, nums) -> bool:
        n = len(nums)
        if n == 1: return True
        
        choose_first = self.choose_helper(nums, 1, n - 1, nums[0])
        choose_last = self.choose_helper(nums, 0, n - 2, nums[-1])

        return choose_first >= 0 or choose_last >= 0
