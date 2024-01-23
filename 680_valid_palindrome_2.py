class Solution:
    def valid_helper(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1
        
        return True

    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        left = 0
        right = n - 1
        while left < right:
            if s[left] != s[right]:
                return self.valid_helper(s, left, right - 1) or self.valid_helper(s, left + 1, right)

            left += 1
            right -= 1
        
        return True
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.validPalindrome("aba"))
    print(sol.validPalindrome("abca"))
    print(sol.validPalindrome("abc"))

# Use 2 pointers to check for a valid palindrome.
# If the two pointers don't match, split 2 different scenarios where you cut one of the pointers out
# and compare the rest. If they still don't match then return false. Otherwise return true if one of the
# scenarios return true

# left = 0
# right = n - 1
# while left < right:
    # if s[left] != s[right] then return helper(left, right - 1) or helper(left + 1, right)
    # left -= 1, right += 1
# return true
    
# helper:
# while left < right:
    # if s[left] != s[right] then return false
    # left -=1, right += 1
# return true