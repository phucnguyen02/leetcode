class Solution:
    def symmetry(self, s):
        n = len(s)
        dp = [[-float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1 if s[i] == 0 else 0
        for d in range(1, n):
            for i in range(n - d):
                j = d + i
                if s[i] + s[j] == 0 and dp[i + 1][j - 1] > 0:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        

        def trace(i, j):
            if i > j: return []
            if i == j: 
                return [s[i]] if s[i] == 0 else []
            if dp[i][j] != dp[i + 1][j] and dp[i][j] != dp[i][j - 1] and dp[i][j] == 2 + dp[i + 1][j - 1]: 
                lst = [s[i]]
                lst.extend(trace(i + 1, j - 1))
                lst.append(s[j])
                return lst
            lst1 = lst2 = []

            if dp[i][j] == dp[i + 1][j]: lst1 = trace(i + 1, j)
            if dp[i][j] == dp[i][j - 1]: lst2 = trace(i, j - 1)

            return lst1 if lst1 else lst2

        print(trace(0, n- 1))
        return dp[0][n - 1]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.symmetry([2,-1,0,3,-2,0,1,2,0,-2,-3,1]))
    print(sol.symmetry([1,1,1,1,1]))