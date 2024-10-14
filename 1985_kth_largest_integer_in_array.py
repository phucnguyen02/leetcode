import heapq

class Solution:
    def kthLargestNumber(self, nums, k: int) -> str:
        int_nums = [int(num) for num in nums]
        heap = int_nums[:k]
        heapq.heapify(heap)
        for num in int_nums[k:]:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        return str(heap[0])
    
# Put the elements into a min heap. Prevent the heap's size from exceeding k by only pushing elements larger than the current head and popping the head.