from itertools import pairwise

class Solution:
    def findMinDifference(self, timePoints) -> int:
        for (i, time) in enumerate(timePoints):
            hour, minute = time.split(":")
            timePoints[i] = int(hour)*60 + int(minute)
        timePoints.sort()
        timePoints.append(timePoints[0] + 1440)
        res = min([(b - a) % 1440 for a, b in pairwise(timePoints)])
        return res
    
if __name__ == "__main__":
    sol = Solution()
    # print(sol.findMinDifference(["23:59","00:00"]))
    # print(sol.findMinDifference(["23:59","00:00", "00:00"]))
    # print(sol.findMinDifference(["01:01","02:01"]))
    print(sol.findMinDifference(["02:39","10:26","21:43"]))
        