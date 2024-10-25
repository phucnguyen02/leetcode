import collections

class Solution:
    def maxSlidingWindow(self, nums, k: int):
        queue = collections.deque()
        l = r = 0
        res = []
        while r < len(nums):
            while queue and nums[r] > nums[queue[-1]]:
                queue.pop() 
            queue.append(r)

            if queue and l > queue[0]:
                queue.popleft()

            if r >= k - 1:
                res.append(nums[queue[0]])
                l += 1

            r += 1
        return res


# Use a monotonically decreasing deque to keep track of the max of a window, with the leftmost element being the largest one.
# Append the indices. If the front of the queue is out of bounds of the window (check based on index), then pop it.