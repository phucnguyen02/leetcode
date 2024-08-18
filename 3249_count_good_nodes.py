from collections import defaultdict

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

class Solution:
    def dfs(self, root):
        if not root.children:
            self.res += 1
            return 1
        
        base_size = -1
        good = True
        total_size = 1
        for child in root.children:
            child_size = self.dfs(child)
            if child_size != base_size:
                if base_size == -1:
                    base_size = child_size
                else:
                    good = False

            total_size += child_size
        
        if good: self.res += 1
        return total_size
    
    def countGoodNodes(self, edges) -> int:
        self.res = 0
        max_val = max([max(x1, x2) for (x1, x2) in edges])
        nodes = [TreeNode(i) for i in range(max_val + 1)]
        has_parent = defaultdict(int)
        for (x1, x2) in edges:
            if x1 == 0 or x2 == 0:
                if x1 == 0:
                    nodes[x1].children.append(nodes[x2])
                    has_parent[x2] = True

                else:
                    nodes[x2].children.append(nodes[x1])
                    has_parent[x1] = True

            else:
                if x1 in has_parent:
                    nodes[x1].children.append(nodes[x2])
                    has_parent[x2] = True
                else:
                    nodes[x2].children.append(nodes[x1])
                    has_parent[x1] = True

        self.dfs(nodes[0])
        return self.res


if __name__ == "__main__":
    sol = Solution()
    print(sol.countGoodNodes([[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]))
    print(sol.countGoodNodes([[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]]))
    print(sol.countGoodNodes([[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]]))