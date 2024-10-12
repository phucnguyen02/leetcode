from collections import deque

class Solution:
    def valid(self, grid, r, c):
        n = len(grid)
        return 0 <= r < n and 0 <= c < n
    
    def shortestPathBinaryMatrix(self, grid) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1
        queue = deque([])
        n = len(grid)
        queue.append((0, 0))
        directions = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, -1), (-1, 1)]
        grid[0][0] = 1
        while queue:
            r, c = queue.popleft()
            if r == n - 1 and c == n - 1:
                return grid[-1][-1]
            for dr, dc in directions:
                new_r = dr + r
                new_c = dc + c
                if self.valid(grid, new_r, new_c) and grid[new_r][new_c] == 0:
                    grid[new_r][new_c] = grid[r][c] + 1
                    queue.append((new_r, new_c))
        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestPathBinaryMatrix([[0,1],[1,0]]))
    print(sol.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))
    print(sol.shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]))
    print(sol.shortestPathBinaryMatrix([[0,0,1,0,1,1],[1,0,0,1,0,0],[0,1,0,1,0,0],[1,0,1,0,0,0],[0,1,0,1,0,0],[0,0,0,0,0,0]]))

# Do BFS to find the shortest path. For each step of the path, mark the square we traverse to the length of the path to get to it to avoid revisiting.