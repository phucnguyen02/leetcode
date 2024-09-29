class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        start, end = 0, 0
        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                end = i + 1
        for d in range(2, n):
            for i in range(n - d):
                j = d + i
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    end = j

        return s[start:end + 1]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("babad"))
    print(sol.longestPalindrome("cbbd"))

# dp(i, j) is whether the substring from i to j forms a palindrome. At first, dp(i, i) = true and dp(i, i + 1) = true if they're the same
# Then, fill out the dp table diagonally. if s[i] == s[j] and the substring without those 2 characters is a palindrome, then the one with them would also be a palindrome.