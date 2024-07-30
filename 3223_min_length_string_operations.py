from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) < 3: return len(s)
        freq = Counter(s)
        res = len(s)

        for ch in freq:
            if freq[ch] > 2:
                if freq[ch] % 2 == 0: res -= freq[ch] - 2
                else: res -= freq[ch] - 1

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumLength("abaacbcbb"))
    print(sol.minimumLength("aa"))

# Since we're deleting 2 characters at a time and we only delete characters if there's multiple of them on both ends of the character,
# we keep track of which characters appear more than 3 times and reduce their counts to 1 or 2.
