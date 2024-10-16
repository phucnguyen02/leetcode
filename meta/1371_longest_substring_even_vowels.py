class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {"a": 1, "e": 2, "i": 4, "o": 8, "u": 16}
        res = 0
        mask = 0
        mask_index = {0: -1}
        for (i, ch) in enumerate(s):
            if ch in vowels:
                mask ^= vowels[ch]
            
            if mask in mask_index:
                res = max(res, i - mask_index[mask])
            else:
                mask_index[mask] = i
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.findTheLongestSubstring("eleetminicoworoep"))
    print(sol.findTheLongestSubstring("leetcodeisgreat"))
    print(sol.findTheLongestSubstring("bcbcbc"))

# Use a bitmask of length 5 to represent the state of a prefix.
# The bitmask represents if the prefix has an even count for each vowel, with 0 being odd and 1 being even. For example, 00001 means "a" has an odd count and the rest have even counts.
# Ideally, we want to find the longest subarray with bitmask 00000
# Otherwise, if there are 2 prefixes with the same bitmask, then the middle subarray has bitmask 00000.