class Solution:
    def maxOperations(self, s: str) -> int:
        s += "1"
        res = 0
        one_count = 0
        gap = False
        for i in range(len(s)):
            if s[i] == "1": 
                if gap: res += one_count
                one_count += 1
                gap = False
            else:
                gap = True
        return res


# If we encounter a 1 after going through some number of 0s, we can maximize the number of operations by moving every 1 before that in order from right to left
# For example, 111001, we encounter the 1 at i = 5, so we keep track of the number of 1s we saw before that and add it to our operations counter.
# We add a 1 to the end of the original string to cover the case in which the last digit is a 0, that way we get in any remaining operations
