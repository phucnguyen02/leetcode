from collections import Counter

class Solution:
    def reportSpam(self, message, bannedWords) -> bool:
        banned = Counter(bannedWords)
        res = 0
        for msg in message:
            res += 1 if msg in banned else 0
            if res >= 2: return True
        return False
    
# Usee a hash map to quickly look up banned words. Stop the moment we get to 2 spam words to save time on big test cases