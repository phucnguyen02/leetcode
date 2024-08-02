class Solution:
    def get_digits(self, num):
        cnt = 0
        while num:
            num //= 10
            cnt += 1
        return cnt
    
    def findNumbers(self, nums) -> int:
        return len([num for num in nums if self.get_digits(num) % 2 == 0])
    
# See what numbers have an even number of digits