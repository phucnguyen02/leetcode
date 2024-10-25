DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def shortestBridge(self, grid) -> int:
        n = len(grid)
        start_r, start_c = 0, 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    start_r = i
                    start_c = j
                    break
            
        
        visited = set()
        queue = []
        def dfs(r, c):
            visited.add((r, c))
            queue.append((r, c, 0))
            grid[r][c] = 2

            for dr, dc in DIRECTIONS:
                new_r = r + dr
                new_c = c + dc
                if not (0 <= new_r < len(grid) and 0 <= new_c < len(grid)):
                    continue

                if (new_r, new_c) in visited:
                    continue

                if grid[new_r][new_c] == 0:
                    continue
                dfs(new_r, new_c)

        dfs(start_r, start_c)
        visited = set()
        while queue:
            r, c, dist = queue.pop(0)
            
            for dr, dc in DIRECTIONS:
                new_r = r + dr
                new_c = c + dc  
                
                if not (0 <= new_r < n and 0 <= new_c < n):
                    continue
                

                if (new_r, new_c) in visited:
                    continue
                
                if grid[new_r][new_c] == 1:
                    return dist
                
                if grid[new_r][new_c] != 0:
                    continue
                
                
                visited.add((new_r, new_c))
                queue.append((new_r, new_c, dist + 1))

        return -1
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestBridge([[0,1],[1,0]]))
    print(sol.shortestBridge([[0,1,0],[0,0,0],[0,0,1]]))
    print(sol.shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))