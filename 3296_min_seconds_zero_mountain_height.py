import heapq

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes) -> int:
        heap = [(t, t, 1) for i, t in enumerate(workerTimes)]
        heapq.heapify(heap)
        while mountainHeight > 1:
            cur, work_time, height_reduced = heapq.heappop(heap)
            heapq.heappush(heap, (cur + work_time * (height_reduced + 1), work_time, height_reduced + 1))
            mountainHeight -= 1
        return heapq.heappop(heap)[0] 

if __name__ == "__main__":
    sol = Solution()
    print(sol.minNumberOfSeconds(4, [2, 1, 1]))
    print(sol.minNumberOfSeconds(10, [3, 2, 2, 4]))
    print(sol.minNumberOfSeconds(5, [1]))

# Use a min heap to keep track of the max time it'll take for the front worker to take down another unit of height