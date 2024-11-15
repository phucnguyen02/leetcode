from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = Counter(s)
        odd = False
        for key, val in count.items():
            if val % 2 != 0:
                if not odd:
                    odd = True
                else:
                    return False

        return True
    
# If there's more than 1 character with an odd count then return False