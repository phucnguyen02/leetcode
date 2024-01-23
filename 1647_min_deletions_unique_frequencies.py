from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        freq_count = Counter([val for val in count.values()])
        freq = [(val, letter) for (letter, val) in count.items()]
        freq.sort(reverse=True)

        res = 0
        for (val, letter) in freq:
            if freq_count[val] != 1:
                freq_count[val] -= 1
                while val and val in freq_count:
                    val -= 1
                    res += 1
                if val: freq_count[val] = 1
        
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.minDeletions("aab"))
    print(sol.minDeletions("aaabbbcc"))
    print(sol.minDeletions("ceabaacb"))

# Sort the frequencies in decreasing order
# Go by most frequent, keep deleting the same character until its frequency is unique, repeat until every frequency is unique
    