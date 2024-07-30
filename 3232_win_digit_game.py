class Solution:
    def count_digits(self, num):
        res = 0

        while num:
            num //= 10
            res += 1
        
        return res
    
    def canAliceWin(self, nums) -> bool:
        odd_sum = 0
        even_sum = 0

        for num in nums:
            digits = self.count_digits(num)
            if digits % 2 == 0:
                even_sum += num
            
            else:
                odd_sum += num

        return even_sum != odd_sum
    
# Check the digit count of every number and add the number to the corresponding sum.
# If one sum is larger than the other then Alice wins, because the game only lasts 1 turn.
