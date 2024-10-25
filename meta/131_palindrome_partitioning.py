class Solution:
    def partition(self, s: str):
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True

        for d in range(2, n):
            for i in range(n - d):
                j = i + d
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True

        res = []
        def backtracking(index, part):
            if index == len(s):
                res.append(part[:])

            for i in range(index, len(s)):
                if dp[index][i]:
                    part.append(s[index:i + 1])
                    backtracking(i + 1, part)
                    part.pop()
        backtracking(0, [])
        return res

#Do DP to find all of the valid palindromes within s. dp(i, j) = True when s[i:j + 1] is a palindrome
# Do backtracking based on that DP. Only do backtracking based on a substring if the substring is a palindrome
