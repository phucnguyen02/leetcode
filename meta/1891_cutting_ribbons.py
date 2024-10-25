class Solution:
    def cuttable(self, ribbons, length, k):
        count = 0
        for ribbon in ribbons:
            count += ribbon // length
        return count >= k
    def maxLength(self, ribbons, k: int) -> int:
        left = 1
        right = max(ribbons) + 1

        while left < right:
            mid = (left + right) // 2
            if not self.cuttable(ribbons, mid, k):
                right = mid
            else:
                left = mid + 1

        return left - 1
            

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxLength([9,7,5], 3))
    print(sol.maxLength([7, 5, 9], 4))
    print(sol.maxLength([5, 7, 9], 22))

# Since we're finding the maximum ribbon length such that we can cut at least k ribbons, do binary search to find the
# smallest ribbon length such that we can't cut k ribbons, and minus 1. The search space should be 1 to the max ribbon length + 1 because we're subtracting 1
# at the end, and the result could be the actual max ribbon length of the original ribbons array