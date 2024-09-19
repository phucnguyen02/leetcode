class Solution:
    def score_recursion(self, a, b, a1, b1):
        if a1 == len(a): return 0
        if b1 == len(b): return -float('inf')
        if (a1, b1) in self.memo:
            return self.memo[(a1, b1)]
        
        take = self.score_recursion(a, b, a1 + 1, b1 + 1) + a[a1] * b[b1]
        not_take = self.score_recursion(a, b, a1, b1 + 1)

        self.memo[(a1, b1)] = max(take, not_take)
        return self.memo[(a1, b1)]
    
    def maxScore(self, a, b) -> int:
        self.memo = {}
        return self.score_recursion(a, b, 0, 0)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxScore([3, 2, 5, 6], [2,-6,4,-5,-3,2,-7]))

# For each index b, there's 2 options. Either you use it to multiply with the current index of a, or you skip it and find a better index.
# We try to find the maximum knowing that. Use a dict for memoization