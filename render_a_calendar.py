import heapq

class Solution:
    def render_calendar(self, dates):
        dates.sort()
        pq = []
        res = 1
        heapq.heappush(pq, dates[0][1])
        for date in dates[1:]:
            if pq[0] < date[0]:
                heapq.heappop(pq)
            heapq.heappush(pq, date[1])
            res = max(len(pq), res)
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.render_calendar([[1, 5], [6, 10], [11, 13], [14, 15], [1, 7], [8, 9], [12, 15], [4, 5], [9, 17]]))
    print(sol.render_calendar([[1, 10], [2, 4], [5, 7]]))

#Using priority queue in order to check how many overlapping dates there are.
#First we sort the dates by the start time and add the first date's end time into the PQ.
#We then check every date after that and compare the start time of a date to the head of the
#PQ's time. If it is smaller, we know that the 2 dates overlap, thus the length of the PQ would increase.
#Otherwise, we pop the PQ.
#We have to compare with the date with the smallest end in order to maximize the number of overlapping events.

#Pseudocode:
#Sort the dates
#Push the end time of the 1st date onto the PQ.
#For i = 1, ..., n-1:
#If pq[0] < dates[i][0] then pop PQ
#Push dates[i][1] to PQ
#Maximize result with length of PQ
#Return result