import heapq
from collections import defaultdict

class Solution:
    def k_largest(self, nums, k, end):
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:end]:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        return heap
    
    def k_smallest(self, nums, k, end):
        heap = [-num for num in nums[:k]]
        heapq.heapify(heap)
        for num in nums[k:end]:
            if -heap[0] > num:
                heapq.heappop(heap)
                heapq.heappush(heap, -num)

        return heap
    
    def medianSlidingWindow(self, nums, k: int):
        if k == 1: return nums
        max_heap = self.k_smallest(nums, k // 2, k) if k % 2 == 0 else self.k_smallest(nums, k // 2 + 1, k)
        min_heap = self.k_largest(nums, k // 2, k)
        removed = defaultdict(int)
        median = 1
        if k % 2 == 0:
            median = (-max_heap[0] + min_heap[0]) / 2
        else:
            median = -max_heap[0]
        res = []
        res.append(median)
        for i in range(k, len(nums)):
            prev = nums[i - k]
            removed[prev] += 1

            balance = -1 if prev <= median else 1
            if nums[i] <= median:
                balance += 1
                heapq.heappush(max_heap, -nums[i])
            else:
                balance -= 1
                heapq.heappush(min_heap, nums[i])

            if balance < 0:
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
            elif balance > 0:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))

            while max_heap and removed[-max_heap[0]] > 0:
                removed[-max_heap[0]] -= 1
                heapq.heappop(max_heap)

            while min_heap and removed[min_heap[0]] > 0:
                removed[min_heap[0]] -= 1
                heapq.heappop(min_heap)

            if k % 2 == 0:
                median = (-max_heap[0] + min_heap[0]) / 2
            else:
                median = -max_heap[0]

            res.append(median)
        return res
if __name__ == "__main__":
    sol = Solution()
    print(sol.medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
    #print(sol.medianSlidingWindow([1,2,3,4,2,3,1,4,2], 3))


# Have a min heap that stores the largest k/2 elements in a window, and have a max heap that stores the smallest k/2 elements (k/2 + 1 if k is odd).
# The median is the top of the max heap or the average of the tops of the max + min heap. We calculate the median much more easily if we retrieve the top since it's O(1).
# Each time we move the window, we add the removed element into a hash table so that we may remove it from our heaps later.
# We also keep track of the "balance" of the heaps. Ideally, both heaps should have the same size or the max heap should have at most 1 more element than the min heap.

# If the removed element was in the max heap (less than the median) then the balance is -1 (representing the fact that we need an extra element in the max heap).
# Otherwise, it's 1 because we need an extra element in the min heap.

# Now we add a new element into one of the heaps. If it's less than the median then it should be in the max heap, and we increment the balance. Otherwise, put it in the min heap and decrement the balance.
# We observe that if the balance is not 0 then an element has to be moved from the larger heap to the smaller heap.
# We should also pop elements from the tops of the heaps if they should have been removed based on the pre-established hash table.
# Continue calculating the median like before.
