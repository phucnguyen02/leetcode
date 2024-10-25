from collections import defaultdict

DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

class Solution(object):
    def largestIsland(self, grid):
        n = len(grid)
        def dfs(r, c, index):
            nonlocal n
            grid[r][c] = index
            total_area = 1

            for dr, dc in DIRECTIONS:
                new_r = r + dr
                new_c = c + dc

                if not (0 <= new_r < n and 0 <= new_c < n):
                    continue

                if grid[new_r][new_c] != 1:
                    continue

                total_area += dfs(new_r, new_c, index)
            
            return total_area

        area = defaultdict(int)
        index = 2
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area[index] = dfs(i, j, index)
                    index += 1
        
        res = max(area.values()) if area else 0

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    neighbors = set()
                    for dr, dc in DIRECTIONS:
                        new_r = r + dr
                        new_c = c + dc

                        if not (0 <= new_r < n and 0 <= new_c < n):
                            continue

                        if grid[new_r][new_c] == 0:
                            continue
                        
                        neighbors.add(grid[new_r][new_c])
                    
                    surround_sum = 0
                    for neighbor in neighbors:
                        surround_sum += area[neighbor]
                    
                    res = max(res, surround_sum + 1)
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.largestIsland([[1,0],[0,1]]))
    print(sol.largestIsland([[1,1],[1,1]]))
# Do DSU to get the size of each island
# Set the coords of the cells with 1 to be the root. This will be the identifier for an island
# Go through all the 0 cells, and check the neighbors. Add up the sizes of the unique islands + 1