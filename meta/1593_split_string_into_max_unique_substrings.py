class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        res = 0

        def backtracking(index, substrings):
            nonlocal res
            if len(substrings) + (len(s) - index) <= res:
                return
            if index == len(s):
                res = max(res, len(substrings))
                return
            
            for i in range(index, len(s)):
                substr = s[index:i + 1]
                if substr not in substrings:
                    substrings.add(substr)
                    backtracking(i + 1, substrings)
                    substrings.remove(substr)

        backtracking(0, set())
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxUniqueSplit("ababccc"))
    print(sol.maxUniqueSplit("aba"))

# Do backtracking to get every possible combination of substrings, while storing them in a set
# If a substring is already in the set, skip over it. Otherwise, add it onto the set and recurse on the index after

# Optimization:
# At any point start, the maximum number of remaining substrings is len(s) - start, because we consider every letter to be a possible substring
# If our current count + the max number of remaining substrings is < max_count, then there's no point in continuing down that path

