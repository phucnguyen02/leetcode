class Solution:
    def valid_coords(self, grid, r, c):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "1"
    
    def dfs(self, grid, r, c):
        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        grid[r][c] = "-1"

        for (dr, dc) in directions:
            new_r = r + dr
            new_c = c + dc
            if self.valid_coords(grid, new_r, new_c):
                self.dfs(grid, new_r, new_c)

    def numIslands(self, grid) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res += 1
                    self.dfs(grid, i, j)

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
    print(sol.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
    
# We want to visit island tiles, aka tiles with 1.
# When we come across an island tile, do a dfs on it and mark the entire island as -1 so we don't visit already explored tiles. Also increase the number of islands.
