class Solution:
    def valid_coords(self, grid, r, c, land):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) in land
        
    def dfs(self, grid, r, c, seen, land):
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        seen.add((r, c))
        grid[r][c] = 4
        
        for (dr, dc) in dir:
            new_r = r + dr
            new_c = c + dc
            
            if self.valid_coords(grid, new_r, new_c, land):
                grid[r][c] -= 1
                if (new_r, new_c) not in seen:
                    self.dfs(grid, new_r, new_c, seen, land)

    def islandPerimeter(self, grid) -> int:
        lr = lc = 0
        land = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    land.add((r, c))
                    lr = r
                    lc = c
        self.dfs(grid, lr, lc, set(), land)
        return sum([sum(arr) for arr in grid])
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
    print(sol.islandPerimeter([[1]]))
    print(sol.islandPerimeter([[0,1,1],[1,1,1],[0,1,0]]))


# The idea behind calculating the perimeter of the island is that each tile of land at first is worth
# 4 perimeter units. However, the more land neighbors it has, the less perimeter units it has. If
# 2 land tiles are next to each other then they're only worth 3 perimeter units each. We
# will use this concept to find the perimeter of the island

# First, add every land tile into a set so we can track it later
# Then, dfs on one of the land tiles. Every land tile at the end should have a value corresponding
# to its perimeter units. As a result, at first, each land tile/element has a value of 4.
# Then, we check each of its neighbors. If a neighbor is a land tile, the current tile's
# value is decremented. We repeat until every land tile has been explored.
# At the end, add up the entire matrix to get the perimeter of the island.
