from collections import Counter
import math

class Solution:
    def minStickers(self, sticker, word) -> int:
        sticker_count = Counter(sticker)
        word_count = Counter(word)
        res = 0
        for letter in word_count:
            if letter not in sticker_count: return -1

            res = max(res, math.ceil(word_count[letter] / sticker_count[letter]))
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minStickers("banaasiofdjsodifjhsodif", "banana"))