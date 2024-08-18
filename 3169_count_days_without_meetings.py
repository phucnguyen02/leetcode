class Solution:
    def countDays(self, days: int, meetings) -> int:
        meetings.sort()
        last = meetings[0][1]
        res = 0
        for meeting in meetings[1:]:
            if last < meeting[0]:
                res += meeting[0] - last - 1
            last = max(last, meeting[1])

        return res + days - last + meetings[0][0] - 1
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.countDays(10, [[5,7],[1,3],[9,10]]))
    print(sol.countDays(5, [[2,4],[1,3]]))
    print(sol.countDays(6, [[1,6]]))
    print(sol.countDays(8, [[3,4],[4,8],[2,5],[3,8]]))