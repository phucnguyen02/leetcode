class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        temp = x

        reversed = 0
        while temp:
            temp, remainder = divmod(temp, 10)
            reversed = reversed * 10 + remainder

        return x == reversed

        
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(1221))

# If the number is negative then it's not a palindrome
# Extract the digits from right to left with divmod and add them up into a reversed number
# Check if the reversed number is equal to the original