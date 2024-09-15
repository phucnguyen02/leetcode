from collections import deque

class Solution:
    def findSafeWalk(self, grid, h: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        vis = [[0 for _ in range(n)] for _ in range(m)]
        memo = {}
        def dfs(x, y, res):
            if x<0 or x>=m or y>=n or y<0 or vis[x][y]==1 or res>=h:
                return float('inf')

            if x==m-1 and y==n-1:
                return res+grid[x][y]

            if (x,y,res) in memo:
                return memo[(x,y,res)]

            vis[x][y] = 1
            
            memo[(x,y,res)] = min(dfs(x+1,y,res+grid[x][y]),dfs(x-1,y,res+grid[x][y]),dfs(x,y+1,res+grid[x][y]),dfs(x,y-1,res+grid[x][y]))
            vis[x][y] = 0
            return memo[(x,y,res)]
        a = dfs(0,0,0)
        print(memo)
        return a-h<0

if __name__ == "__main__":
    sol = Solution()
    print(sol.findSafeWalk([[0,1],[0,1]], 3))

# Use a dict to store the health it takes to get to each square given a path, then for each square, take the minimum it takes to get to its neighbors
