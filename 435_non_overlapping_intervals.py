class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        intervals.sort(key=lambda x: x[1])
        res = 0
        prev_end = intervals[0][1]
        for interval in intervals[1:]:
            if prev_end > interval[0]:
                res += 1
            else:
                prev_end = interval[1]
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
    print(sol.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))

# Sort the intervals by their end times
# Store the last interval's end time. Compare it with the start times of the next intervals. If the end is larger than the start then there's an overlap.
# Otherwise, update the last interval's end time.