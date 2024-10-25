import heapq
from collections import deque

class Solution:
    def longestSubarray(self, nums, limit: int) -> int:
        max_heap = []
        min_heap = []
        removed = set()

        left = 0
        res = 1
        for right in range(len(nums)):
            heapq.heappush(max_heap, (-nums[right], right))
            heapq.heappush(min_heap, (nums[right], right))

            while (-max_heap[0][0] - min_heap[0][0]) > limit:
                removed.add(left)
                left += 1
                while max_heap and max_heap[0][1] in removed:
                    heapq.heappop(max_heap)

                while min_heap and min_heap[0][1] in removed:
                    heapq.heappop(min_heap)
            
            res = max(right - left + 1, res)

        return res
    
    def longestSubarray(self, nums, limit: int) -> int:
        max_deque = deque()
        min_deque = deque()
        left = 0
        res = 1
        for right in range(len(nums)):
            while max_deque and nums[max_deque[-1]] < nums[right]:
                max_deque.pop()

            max_deque.append(right)

            while min_deque and nums[min_deque[-1]] > nums[right]:
                min_deque.pop()

            min_deque.append(right)
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                if max_deque and max_deque[0] == left:
                    max_deque.popleft()
                
                if min_deque and min_deque[0] == left:
                    min_deque.popleft()
                left += 1
                
            
            res = max(right - left + 1, res)

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestSubarray([8,2,4,7], 4))
    print(sol.longestSubarray([10,1,2,4,7,2], 5))
    print(sol.longestSubarray([4,2,2,2,4,4,2,2], 0))

# Similar to Sliding Window Maximum, keep mono increasing + decreasing deques to store the max/min for a sliding window.
# Increase the window size until the difference between the front of these 2 deques is larger than the limit.
# Then, move the left pointer rightward and pop the deques if the left index matches the fronts