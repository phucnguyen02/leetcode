class DSU:
    def __init__(self, n):
        self.size = [1]*n
        self.parent = [i for i in range(n)]

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u != v:
            if self.size[u] < self.size[v]:
                u, v = v, u
            
            self.parent[v] = u
            self.size[u] += v
        