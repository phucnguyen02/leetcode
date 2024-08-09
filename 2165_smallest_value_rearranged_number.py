class Solution:
    def digits_to_num(self, digits):
        num = 0
        for digit in digits:
            num = num * 10 + digit
        
        return num
    
    def smallestNumber(self, num: int) -> int:
        if not num: return 0
        digits = [int(x) for x in str(abs(num))]
        if num < 0:
            digits.sort(reverse=True)
        else:
            digits.sort()
            if digits[0] == 0:
                for (i, digit) in enumerate(digits):
                    if digit:
                        digits[0], digits[i] = digits[i], digits[0] 
                        break
            
        return self.digits_to_num(digits) if num >= 0 else -self.digits_to_num(digits) 
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.smallestNumber(31000000))
    print(sol.smallestNumber(-7605))

# Parse the number into an array of its digits
# If it's a negative number, sort the array in descending order. Positive? Ascending.
# In the case of a positive number and the digits array starts with a 0, we find the first number in the array that isn't 0 and swap it with the 0, then it's the smallest number
# Return the sorted digits array with the appropriate sign