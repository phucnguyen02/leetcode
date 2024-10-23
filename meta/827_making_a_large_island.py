class DSU:
    def __init__(self, grid, m, n):
        self.parent = {(i, j): (i, j) for i in range(m) for j in range(n)}
        self.size = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.size[(i, j)] = 1
                else:
                    self.size[(i, j)] = 0

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u != v:
            if self.size[u] < self.size[v]:
                self.parent[u] = v
                self.size[v] += self.size[u]
            else:
                self.parent[v] = u
                self.size[u] += self.size[v]

class Solution:  
    def largestIsland(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        uf = DSU(grid, m, n)
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    grid[r][c] = -1
                    for (dr, dc) in directions:
                        new_r = r + dr
                        new_c = c + dc
                        if 0 <= new_r < m and 0 <= new_c < n and grid[new_r][new_c] == 1:
                            uf.union((r, c), (new_r, new_c))

        for r in range(m):
            for c in range(n):
                if grid[r][c] == -1:
                    grid[r][c] = uf.find((r, c))

        res = max(uf.size.values() or 0)
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    sum = 0
                    seen = set()
                    for (dr, dc) in directions:
                        new_r = r + dr
                        new_c = c + dc
                        if 0 <= new_r < m and 0 <= new_c < n and grid[new_r][new_c] != 0:
                            seen.add(grid[new_r][new_c])
                    for d in seen:
                        sum += uf.size[d]
                    res = max(res, sum + 1)

        return res

# Do DSU to get the size of each island
# Set the coords of the cells with 1 to be the root. This will be the identifier for an island
# Go through all the 0 cells, and check the neighbors. Add up the sizes of the unique islands + 1