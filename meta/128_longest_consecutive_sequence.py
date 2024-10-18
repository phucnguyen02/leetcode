from collections import defaultdict

class DSU:
    def __init__(self, nums):
        self.size = defaultdict(int)
        self.parent = defaultdict(int)
        for num in nums:
            self.parent[num] = num
            self.size[num] = 1

    def find(self, u):
        if self.parent[u] == u: return u
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
    def longestConsecutive_B(self, nums) -> int:
        if not nums: return 0
        count = set(nums)
        uf = DSU(nums)
        for num in nums:
            if num + 1 in count:
                uf.union(num, num + 1)
            if num - 1 in count:
                uf.union(num, num - 1)
        res = uf.size.values()
        return max(res)
    
    def longestConsecutive(self, nums) -> int:
        if not nums: return 0
        res = 0
        num_set = set(nums)
        for num in num_set:
            streak = 0
            if num - 1 not in num_set:
                while num in num_set:
                    num += 1
                    streak += 1
                res = max(res, streak)
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive([100,4,200,1,3,2]))
    print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print(sol.longestConsecutive([1,-8,7,-2,-4,-4,6,3,-4,0,-7,-1,5,1,-9,-3]))

# Do DSU to connect 2 consecutive elements together and find the largest connected component

# Or iterate through every number, check if number - 1 is not in the array, that means it's the start of the consecutive sequence.
# Increment the number until it's not in the array anymore. Find the largest number of times you can increment