import math
import heapq

class Solution:
    def kClosest(self, points, k: int):
        dist = [(math.sqrt(x ** 2 + y ** 2), x, y) for (x, y) in points]
        heapq.heapify(dist)
        res = []
        while k:
            dst, x, y = heapq.heappop(dist)
            res.append([x, y])
            k -= 1

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.kClosest([[1,3],[-2,2]], 1))
    print(sol.kClosest([[3,3],[5,-1],[-2,4]], 2))

# Save time:
# Use binary search from 0 to the max distance. For every midpoint, check how many distances are below that midpoint.
# If it's less than k then check the right subarray while reducing k since the remaining distances will be on the right.
# Otherwise, discard the right subarray.
# This is O(N)