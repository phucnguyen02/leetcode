class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for d in range(1, n):
            for i in range(n - d):
                j = d + i
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][-1] >= len(s) - k
    
# It's longest palindromic subsequence but ensure that dp[0][-1] >= len(s) - k, since you can only remove at most k characters from it.