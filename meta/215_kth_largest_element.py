import heapq

class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        return heap[0]

if __name__ == "__main__":
    sol = Solution()
    print(sol.findKthLargest([3,2,1,5,6,4], 2))

# Put the elements into a min heap. Prevent the heap's size from exceeding k by only pushing elements larger than the current head and popping the head.