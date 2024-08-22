class Solution:
    def maxEnergyBoost(self, energyDrinkA, energyDrinkB) -> int:
        n = len(energyDrinkA)
        if n == 1: return max(energyDrinkA[0], energyDrinkB[0])
        dp = [[0 for _ in range(2)] for _ in range(n)]
        dp[0][0] = energyDrinkA[0]
        dp[0][1] = energyDrinkB[0]
        dp[1][0] = sum(energyDrinkA[:2])
        dp[1][1] = sum(energyDrinkB[:2])
        for i in range(2, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 2][1]) + energyDrinkA[i]
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0]) + energyDrinkB[i]
        
        return max(dp[-1])
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxEnergyBoost([1,3,1], [3,1,1]))
    print(sol.maxEnergyBoost([4,1,1], [1,1,3]))

# dp(i, 0) being the max energy you get if you drink the type A's i-th drink, dp(i, 1) being the same but with B instead.
# Base cases: dp(0, 0) = A[0], dp(0, 1) = B[0], dp(1, 0) = A[0] + A[1], dp(1, 1) = B[0] + B[1].
# There's no reason to skip out on the first hour/drink to get a different type when you can just drink 2 of the same type consecutively.
# Recurrence relation: dp(i, 0) = max(dp(i - 1, 0), dp(i - 2, 1)) + A[i],   dp(i, 1) = max(dp(i - 1, 1), dp(i - 2, 0)) + B[i]

# If you drink the i-th drink, you're either drinking the same type again or you skipped the previous hour after drinking from a different type.
# Thus, the max energy would be the max between those 2 scenarios