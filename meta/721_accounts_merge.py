from collections import defaultdict

class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n

    def find(self, u):
        if self.parent[u] == u:
            return u
        return self.find(self.parent[u])

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u != v:
            if self.size[u] > self.size[v]:
                self.parent[v] = u
                self.size[u] += self.size[v]
            else:
                self.parent[u] = v
                self.size[v] += self.size[u]


class Solution:
    def accountsMerge(self, accounts):
        n = len(accounts)
        uf = DSU(n)
        email_group = defaultdict(int)
        for i in range(n):
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]

                if email not in email_group:
                    email_group[email] = i
                else:
                    uf.union(email_group[email], i)
    
        components = defaultdict(list)
        for email in email_group:
            group_index = email_group[email]
            parent = uf.find(group_index)
            components[parent].append(email)
        
        res = []
        for index in components:
            components[index].sort()
            res.append([accounts[index][0]] + components[index])
        return res
if __name__ == "__main__":
    sol = Solution()
    print(sol.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))

# We assign each account to the index of the name in the bigger array. We will do DSU on these indices.
# We store each email to an index. If we come across that email again, we join this index and the index assigned to the email
# After all of the union is done, we check which emails are assigned to the parent of the index in the DSU.
# Sort the lists corresponding to each index that way and add the names to them, which can be traced using the index.