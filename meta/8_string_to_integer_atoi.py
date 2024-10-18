class Solution:
    def myAtoi(self, s: str) -> int:
        if not s: return 0
        sign = 1
        ptr = 0
        res = 0
        while ptr < len(s) and s[ptr] == " ":
            ptr += 1
        
        if ptr >= len(s) or not (s[ptr] in "+-" or s[ptr].isdigit()):
            return res

        if s[ptr] in "+-":
            sign = -1 if s[ptr] == "-" else 1
            ptr += 1
        while ptr < len(s) and s[ptr].isdigit():
            res = res*10 + int(s[ptr])
            ptr += 1
        
        if sign == 1:
            res = min(2 ** 31 - 1, res)
        else:
            res *= -1
            res = max(-2 ** 31, res)
        return res

# Iterate through the first chunk of the array, skipping through whitespaces.
# After that, check the current character. If we're outside of the array or the character is neither a sign or a digit, then we're done
# Check the sign and change the integer according to it (1 being pos, -1 being neg)
# Iterate through the rest of the array until we hit a non-digit, add up res at the same time
# If it's pos, return the min of res and 2^31 - 1, otherwise it's the max of -res and -2 ** 31
# Handle edge cases!!!
# String only has whitespaces