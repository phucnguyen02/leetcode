class Solution:
    def iso(self, s, t):
        if len(s) != len(t): return False
        replace = {}

        for i in range(len(s)):
            ch = s[i]
            if ch in replace and replace[ch] != t[i]: return False
            
            replace[ch] = t[i]
        
        return True
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.iso(s, t) and self.iso(t, s)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.isIsomorphic("egg", "add"))
    print(sol.isIsomorphic("foo", "bar"))
    print(sol.isIsomorphic("paper", "title"))
    print(sol.isIsomorphic("badc", "baba"))

# Keep track of every replacement and if there's a duplicate, we return false. Do this 2 times because one array can be replaced to get the other, but not necessarily vice versa.