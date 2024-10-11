from collections import defaultdict

class Solution:
    def suspicious_dfs(self, node):
        if node in self.suspicious:
            return
        self.suspicious.add(node)
        for neighbor in self.neighbors[node]:
            self.suspicious_dfs(neighbor)

    def regular_dfs(self, node):
        if node in self.visited:
            return
        self.visited.add(node)
        if node in self.suspicious:
            self.suspicious = []
            return
        for neighbor in self.neighbors[node]:
            self.regular_dfs(neighbor)


    def remainingMethods(self, n: int, k: int, invocations):
        self.suspicious = set()
        self.neighbors = defaultdict(list)
        for (x, y) in invocations:
            self.neighbors[x].append(y)

        self.suspicious_dfs(k)
        self.visited = set()
        for node in range(n):
            if node not in self.suspicious:
                self.regular_dfs(node)

        return [node for node in range(n) if node not in self.suspicious]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.remainingMethods(4, 1, [[1,2],[0,1],[3,2]]))
    print(sol.remainingMethods(5, 0, [[1,2],[0,2],[0,1],[3,4]]))
    print(sol.remainingMethods(3, 2, [[1,2],[0,1],[2,0]]))

# Do DFS on a suspicious node and mark all nodes that it can reach as suspicious.
# Do DFS on any other node and see if it can reach the connected component of suspicious nodes