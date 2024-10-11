import heapq

class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        elem = None
        while k:
            elem = heapq.heappop(heap)
            k -= 1
        return -elem

if __name__ == "__main__":
    sol = Solution()
    print(sol.findKthLargest([3,2,1,5,6,4], 2))

# Put the elements into a max heap, pop the heap k times and the last popped element is the k-th largest