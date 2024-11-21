class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = []
        cols = []
        houses = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    rows.append(i)
                    houses.append((i, j))

        for i in range(n):
            for j in range(m):
                if grid[j][i]:
                    cols.append(i)

        median_rows = rows[len(rows) // 2]
        median_cols = cols[len(cols) // 2]

        return sum([abs(house[0] - median_rows) + abs(house[1] - median_cols) for house in houses])
    
# Median of rows and cols is the best meeting point