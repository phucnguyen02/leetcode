class Solution:
    def merge(self, intervals):
        res = []
        intervals.sort()

        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))

# Sort the intervals first. We only add intervals into the result array if it's empty at first or if the end of the last interval is smaller than the start
# of the next interval, because then it'd be 2 separate intervals that don't overlap.
# We update the end of the last interval to be the maximum of the following intervals' ends and the current end, since we know they overlap