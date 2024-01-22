from collections import Counter
import heapq

class Solution:
    def minMeetingRooms(self, intervals) -> int:
        intervals.sort()
        heap = [intervals[0][1]]
        
        for (start, end) in intervals[1:]:
            if start >= heap[0]:
                heapq.heappop(heap)

            heapq.heappush(heap, end)
            heapq.heapify(heap)
        
        return len(heap)

    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minMeetingRooms([[0,30],[5,10],[15,20]]))
    print(sol.minMeetingRooms([[7,10],[2,4]]))
    print(sol.minMeetingRooms([[9,10],[4,9],[4,17]]))
    print(sol.minMeetingRooms([[1,5],[8,9],[8,9]]))

# Sort the meeting rooms by their start times first because we have to compare the start time of the next meeting to the end time of a meeting before it
# Put the intervals into a heap. We only care about the meeting room that is vacant the earliest. If an incoming meeting cannot be allocated for the
# earliest vacant meeting room, then it can't be allocated to any other room.
# By that logic, compare the start time of the incoming meeting to the end time of the meeting that's the earliest. If you can't allocate for that
# meeting then you create a new room for it. Otherwise, replace the ended meeting with the newest meeting.
# Return the length of the heap