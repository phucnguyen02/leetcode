import heapq

class Solution:
    def minGroups(self, intervals) -> int:
        intervals.sort()
        groups = []
        heapq.heappush(groups, intervals[0][1])

        for (start, end) in intervals[1:]:
            if groups[0] < start:
                heapq.heappop(groups)
            
            heapq.heappush(groups, end)

        return len(groups)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]]))

# First sort all the intervals by the start time. Then, use a min heap to store all the end points.
# We want the top of the min heap to reflect the earliest end point of an interval.
# When we process a new interval, compare its start with the top to see if there's an overlap.
# If there isn't, pop the top of the heap. Push the new interval's end into the heap.
# The length of the heap is supposed to represent the maximum number of overlaps at any point.