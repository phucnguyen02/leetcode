class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0]*(days[-1]+1)
        day_set = set(days)
        for i in range(1, len(dp)):
            if i in day_set:
                dp[i] = min(dp[max(i-1, 0)] + costs[0], dp[max(i-7, 0)] + costs[1], dp[max(i-30, 0)] + costs[2])
            else:
                dp[i] = dp[i-1]

        return dp[-1]
        
        
# dp(i) = min(dp(i - 1) + costs[0], dp(i - 7) + costs[1], dp(i - 30) + costs[2]) if i is a travel day
# dp(i) = dp(i - 1) otherwise