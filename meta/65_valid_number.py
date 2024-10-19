from collections import Counter

class Solution:
    def is_integer(self, s):
        ptr = 0
        sign_count = 0
        while ptr < len(s) and s[ptr] in "+-":
            ptr += 1
            sign_count += 1
            if sign_count > 1: return False
        digit = False

        while ptr < len(s):
            if not s[ptr].isdigit(): return False
            ptr += 1
            digit = True

        return digit
    
    def is_decimal(self, s):
        if s == ".": return False
        dot_count = Counter(s)["."]
        if dot_count > 1: return False
        ptr = 0
        sign_count = 0
        digit = False
        while ptr < len(s) and s[ptr] in "+-":
            ptr += 1
            sign_count += 1
            if sign_count > 1: return False

        while ptr < len(s):
            if not s[ptr].isdigit() and s[ptr] != ".": return False
            digit = s[ptr].isdigit() or digit
            ptr += 1
        
        return digit
            
    def isNumber(self, s: str) -> bool:
        tokens = s.split("E") if "E" in s else s.split("e")
        if len(tokens) > 2: return False
        if len(tokens) == 2:
            left = self.is_decimal(tokens[0]) if "." in tokens[0] else self.is_integer(tokens[0])
            right = self.is_integer(tokens[1])
            return left and right
        return self.is_decimal(tokens[0]) if "." in tokens[0] else self.is_integer(tokens[0])
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.isNumber("0"))
    print(sol.isNumber("e"))
    print(sol.isNumber("."))
    print(sol.isNumber("--90E3"))
    print(sol.isNumber("99e2.5"))
    print(sol.isNumber("3."))

# We check whether a specified string is an integer or a decimal and have different cases accounting for them.
# For example, if there is an e in the string, we split the string based on it. If there are more than 2 splits then that
# means there are more than 2 es, so the string isn't a number
# If there is only 1 e, then we check the parts the string got split into.
# The second part has to be an integer, whereas the first can be either an integer or a decimal, depending on if "." is in it
# If there aren't any es, then check if the string is either an integer or a decimal, depending on if "." is in it

# A number can have an optional leading sign at the beginning. So we increment the counter until we've moved past the signs.
# If there is more than 1 sign then it's not valid (--, -+, +-, ++-, etc.)
# For the integer case, we check if the remaining string is full of digits or not. We have to ensure the existence of a digit and that there are only digits.
# For example, a case like "+" would return incorrectly if we forgo the existence of a digit.

# For the decimal case, we first check if there is more than 1 ".". If yes, return false. Next, we do the same as the integer case where we move past the sign
# We also have to ensure the existence of a digit in the remaining string. Iterate through the rest, if a character is not a digit or "." then return false
# Otherwise, return true if there exists a digit in the rest of the string after the iteration.