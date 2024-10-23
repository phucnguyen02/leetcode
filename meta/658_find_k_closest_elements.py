import heapq

class Solution:
    def findClosestElements(self, arr, k: int, x: int):
        heap = [(-abs(num - x), num) for num in arr[:k]]

        for num in arr[k:]:
            cur_diff = abs(num - x)
            if -heap[0][0] == cur_diff:
                if num < heap[0][1]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-cur_diff, num))
            elif -heap[0][0] > cur_diff:
                heapq.heappop(heap)
                heapq.heappush(heap, (-cur_diff, num))
                
        return sorted([i[1] for i in heap])
    
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Initialize binary search bounds
        left = 0
        right = len(arr) - k
        
        # Binary search against the criteria described
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]
    
# Do a binary search to find the first element of the result window. Let this element be arr[mid]
# arr[mid] and arr[mid + k] cannot be in the same window together. Thus, we compare their differences with x.
# If the diff between arr[mid] and x is smaller than arr[mid + k] and x, then arr[mid + k] cannot be in the window, so we shrink right to mid
# Otherwise, shrink left to be mid + 1 as arr[mid] cannot be in the result window when its difference is larger than with arr[mid + k], who it cannot share the window with 
# We do if x - arr[mid] > arr[mid + k] - x since that checks for elements that have the same value the best. If x > arr[mid] then we ideally want to move the pointer from left to right,
# otherwise, move from right to left