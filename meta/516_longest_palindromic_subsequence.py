class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
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

        return dp[0][-1]
    
# If a number in the array is 0 then at first, the longest mirror symmetric subsequence would be itself since the center is 0. 
# If we compare 2 numbers in the array and they are the same, we check the subsequence between those 2 numbers and promptly update the max subsequence length 
# if the subsequence contains a 0. Otherwise, we check the 2 subsequences that do not contain each number respectively and get the max length between them.

# Let $DP[i, j]$ to be the length of the longest mirror symmetric subsequence for the subarray from index $i$ to index $j$. We want to find $DP[1, n]$. By default $DP[i, i]$ is 1 if $S[i] = 0$ and 0 otherwise since if a single number is 0 then itself is a symmetric subsequence.\\
# As mentioned above, if we compare 2 numbers $S[i]$ and $S[j]$ in the array and they are the same, then they can be candidates for a mirror symmetric subsequence. The other condition is that there is a 0 in-between them. We can elegantly check this by checking the subarray between those 2 numbers. If there was a 0 in it, then $DP[i + 1, j - 1]$ would be larger than 0 since it updates based on the max length of the previous mirror symmetric subsequence. And as established above, $DP[i, i] = 1$ if $S[i] = 0$, so the existence of 0 would cause all of the subarrays containing it to have 1 as the smallest possible length for a mirror symmetric subsequence.\\
# Otherwise, we'd get the max mirror symmetric subsequence length of the subarrays that don't contain $S[i]$ and $S[j]$ respectively since those could have different lengths depending on $S[i]$ and $S[j]$ being included in the subarray from $i + 1$ to $j - 1$. And this works if we fill out the DP table diagonally because to fill out $DP[i, j]$, we'd need the entry to the left of it representing $DP[i, j - 1]$, and the entry below it representing $DP[i + 1 ,j]$, and diagonal filling would ensure that those cells have the appropriate minimum values beforehand.\\
# Furthermore, we do not need to worry about cases of $DP[i, j]$ where $i > j$ since the start of a subarray has to be before its end.\\\\