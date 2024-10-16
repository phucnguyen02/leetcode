class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == "*" or p == "*" or p == s: return True
        len_s = len(s)
        len_p = len(p)
        dp = [[False for i in range(len_p + 1)] for j in range(len_s + 1)]
        dp[0][0] = True
        for i in range(1, len_p + 1):
            if p[i - 1] == "*" and dp[0][i - 1]:
                dp[0][i] = True

        for i in range(1, len_s + 1):
            for j in range(1, len_p + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]

                elif p[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        
        return dp[-1][-1]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.isMatch("aa", "a"))
    print(sol.isMatch("aa", "*"))
    print(sol.isMatch("cb", "?a"))
    print(sol.isMatch("abcdde", "a?*e"))

# Recurrence relation: dp(i, j) = whether you can match s[:i + 1] with p[:j + 1]. Initialize with empty string as well for i - 1, j - cases
# dp(0, 0) = True since 2 empty strings match each other.
# If s[i - 1] == p[j - 1] or p[j - 1] == ? then we rely on dp(i - 1, j - 1) to determine whether dp(i, j) is true or not
# If p[j - 1] == "*" then either it can be empty (check dp(i, j - 1)/where you don't include the character in p) or it can replace a character in s (check dp(i - 1, j))

