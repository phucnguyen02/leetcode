class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == "0": return 0
        dp = [0]*n
        dp[0] = 1

        for i in range(1, n):
            if s[i] != "0":
                dp[i] = dp[i - 1]

            if 10 <= int(s[i - 1:i + 1]) <= 26:
                dp[i] += dp[i - 2] if i > 1 else 1

        return dp[-1]
    
    # def numDecodings(self, s: str) -> int:
    #     n = len(s)
    #     if s[0] == "0": return 0
    #     cur = 1
    #     prev = 1
    #     prev_2 = 1
    #     for i in range(1, n):
    #         cur = 0
    #         if s[i] != "0":
    #             cur = prev

    #         if 10 <= int(s[i - 1:i + 1]) <= 26:
    #             cur += prev_2

    #         prev_2 = prev
    #         prev = cur
        
    #     return cur
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.numDecodings("10"))
    # print(sol.numDecodings("12"))
    
    # print(sol.numDecodings("226"))
    # print(sol.numDecodings("06"))

# dp(i) = number of ways to decode up to index i
# Recurrence relation:
# dp(i) += dp(i - 1) if s[i] is nonzero. The reason is that all of the previous valid decoders can now include the current character.
# dp(i) += dp(i - 2) if s[i - 1:i+1] is between 10 and 26. The reason is that all of the previous valid decoders can now include the current 2 characters.
# Very similar to climbing stairs. Could even do this in O(1) memory.

    


