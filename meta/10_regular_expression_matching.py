class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.cache = {}
        def dfs(i, j):
            if (i, j) in self.cache: return self.cache[(i, j)]
            if i >= len(s) and j >= len(p): return True
            if j >= len(p): return False

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if j + 1 < len(p) and p[j + 1] == "*":
                self.cache[(i, j)] = (match and dfs(i + 1, j)) or dfs(i, j + 2)

            elif match:
                self.cache[(i, j)] = dfs(i + 1, j + 1)

            else:
                self.cache[(i, j)] = False
            
            return self.cache[(i, j)]
        
        return dfs(0, 0)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.isMatch("aa", "a"))
    print(sol.isMatch("aa", "a*"))
    print(sol.isMatch("ab", ".*"))

# (i, j) represents if we can match the string up to indices i for s and j for p
# We first check if s[i] == p[j] first and mark a flag accordingly.
# Next, we see if p[j + 1] == "*" so we can decide whether to use multiple or none of p[j]
# We only use p[j] if s[i] == p[j]. And if we use it, we move the i pointer forward and keep j because we might match more of p[j]
# If we don't use the *, we move the j pointer forward by 2 to go to the next character.

# If p[j + 1] != "*" then we move both pointers forward since the current characters are equal already
# If none of this happens we return false