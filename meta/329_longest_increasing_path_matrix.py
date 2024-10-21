from collections import defaultdict

class Solution:
    def dfs(self, matrix, r, c):
        if (r,c) in self.cache: return self.cache[(r, c)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            new_r = r + dr
            new_c = c + dc
            if 0 <= new_r < len(matrix) and 0 <= new_c < len(matrix[0]) and matrix[new_r][new_c] > matrix[r][c]:
                self.cache[(r, c)] = max(self.dfs(matrix, new_r, new_c), self.cache[(r, c)])

        self.cache[(r, c)] += 1
        return self.cache[(r, c)]
    def longestIncreasingPath(self, matrix) -> int:
        res = 0
        m, n = len(matrix), len(matrix[0])
        self.cache = defaultdict(int)
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(matrix, i, j))

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))

# Do DFS + memoization, while storing the max increasing length of a path starting at (i, j).
# When traversing DFS, only traverse to squares that are larger than the current