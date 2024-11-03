import heapq

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    def minTimeToReach(self, moveTime) -> int:
        heap = [(0, 0, 0, 1)]
        m, n = len(moveTime), len(moveTime[0])
        min_arrive = [[float('inf') for _ in range(n)] for _ in range(m)]
        visited = set()
        while heap:
            time, r, c, prev = heapq.heappop(heap)
            visited.add((r, c))
            if (r, c) == (m - 1, n - 1):
                return time
            for (dr, dc) in DIRECTIONS:
                new_r = r + dr
                new_c = c + dc

                if not (0 <= new_r < m and 0 <= new_c < n): continue

                if (new_r, new_c) in visited: continue

                arrive = max(moveTime[new_r][new_c], time) + prev
                if arrive < min_arrive[new_r][new_c]:
                    min_arrive[new_r][new_c] = arrive
                    heapq.heappush(heap, (arrive, new_r, new_c, 3 - prev))

        return -1
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minTimeToReach([[0,4],[4,4]]))
    print(sol.minTimeToReach([[0,0,0,0],[0,0,0,0]]))
    print(sol.minTimeToReach([[0,24,55,20,92,100,8,70,77,22,50,64,48,45,30,0,28,100,94,28],[67,63,35,86,38,3,31,58,82,15,68,98,69,7,49,73,32,93,54,12],[51,39,70,77,72,54,45,20,27,48,36,56,18,50,22,73,79,18,70,79],[100,54,79,41,2,12,40,84,90,78,42,48,10,29,2,80,94,93,12,11],[2,98,67,85,93,49,71,97,57,3,99,66,94,61,11,54,72,44,70,2],[82,89,87,76,97,55,56,35,86,25,83,38,57,0,82,51,71,66,63,80],[96,35,43,70,26,98,98,77,96,79,60,3,51,78,56,92,51,73,1,40],[55,82,44,9,70,96,55,32,44,17,31,90,23,38,95,26,79,31,89,4],[100,60,47,3,45,72,38,48,78,8,68,25,55,54,69,13,88,2,29,81],[67,9,82,18,49,67,68,49,42,23,74,98,30,72,86,83,32,96,12,78],[64,40,23,59,67,85,42,60,6,96,17,16,94,12,94,44,41,63,93,92],[19,53,23,67,7,31,26,4,62,40,99,68,61,1,81,51,99,66,43,31],[98,82,41,1,63,35,48,9,68,34,76,72,99,91,96,47,82,86,41,10],[77,88,23,28,35,12,65,79,61,62,4,1,97,72,51,31,28,2,3,0]]))

# Dijkstra's to find shortest path. Arrive time is max(cell, current time) + prev. Prev = 3 - prev.
# When switching between 2 integer states, easy way to do it is subtracting the other from their sum