class Solution:
    def intervalIntersection(self, firstList, secondList):
        if not secondList or not firstList: return []
        ptr1 = ptr2 = 0
        res = []
        while ptr1 < len(firstList) and ptr2 < len(secondList):
            start_1, end_1 = firstList[ptr1]
            start_2, end_2 = secondList[ptr2]
            max_start = max(start_1, start_2)
            min_end = min(end_1, end_2)
            if max_start <= min_end:
                res.append([max_start, min_end])
            if end_1 < end_2:
                ptr1 += 1
            else:
                ptr2 += 1
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))

# Use 2 pointers for both list. Take the max start and min end of the 2 pointers to get the intersection. If max start < min end then we have an intersection
# Move the pointer of the interval with the smaller end because moving the one with the bigger while we already don't have an intersection won't get us an intersection
# Furthermore, one pointer would just be stuck.