class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        if not word1 or not word2: return max(len1, len2)
        dp = [[float('inf') for i in range(len1)] for j in range(len2)]
        dp[0][0] = 1 if word1[0] != word2[0] else 0
        found_first = False

        for i in range(1, len1):
            if word1[i] == word2[0] and not found_first:
                found_first = True
                dp[0][i] = dp[0][i - 1]
            else:
                dp[0][i] = dp[0][i - 1] + 1

        found_first = False
        for i in range(1, len2):
            if word2[i] == word1[0] and not found_first:
                found_first = True
                dp[i][0] = dp[i - 1][0]
            else:
                dp[i][0] = dp[i - 1][0] + 1
        
        for i in range(1, len2):
            for j in range(1, len1):
                if word1[j] == word2[i]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        
        return dp[-1][-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.minDistance("", "ros"))
    print(sol.minDistance("horse", "ros"))
    print(sol.minDistance("intention", "execution"))
    print(sol.minDistance("this is a test", "wokka wokka!!!"))

# Variables: dp(i, j) being the minimum number of operations to turn word1 into word2 up to indices j for word1 and i for word2.
    
# Base case: dp(0, 0) = 0 if word1[0] = word2[0] and 1 otherwise.

# Recurrence relation:
# If 2 letters of the strings are the same, then we don't need an additional operation. We can just base the current result on the previous iteration
# of the strings (1 letter before for both). In other words, dp(i, j) = dp(i - 1, j - 1) if word1[j] = word2[i]
    
# Otherwise, take the minimum from the 3 previous iterations and pretend we are adding in another character for the current iteration.
# dp(i, j) = min(dp(i - 1, j), dp(i, j - 1), dp(i - 1, j - 1)) + 1
    
