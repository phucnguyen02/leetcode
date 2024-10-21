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