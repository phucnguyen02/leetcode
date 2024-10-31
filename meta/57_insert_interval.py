from bisect import bisect_left, insort_left
class Solution:
    def insert(self, intervals, newInterval):
        if not intervals: return [newInterval]
        res = []
        insort_left(intervals, newInterval)
        
        #intervals = intervals[:position] + [newInterval] + intervals[position:]
        for (start, end) in intervals:
            if res and res[-1][1] >= start:
                res[-1][1] = max(end, res[-1][1])
            else:
                res.append([start, end])
        return res

    
if __name__ == "__main__":
    sol = Solution()
    print(sol.insert([[1,5]], [0, 1]))
    print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [5, 8]))
    print(sol.insert([[2,3],[5,7]], [0, 6]))
    print(sol.insert([[1,5]], [6, 8]))
    
# Use binary search to find where to fit the interval, sorted based on starting time
# Go through every interval and slowly add them to the result array. If a new interval were to be added but it overlaps with the most recent one, maximize the end.