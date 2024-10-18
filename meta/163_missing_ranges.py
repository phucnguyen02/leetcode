class Solution:
    def findMissingRanges(self, nums, lower: int, upper: int):
        if not nums: return [[lower, upper]]
        low = []
        high = []
        if lower < nums[0]: low = [lower, nums[0] - 1]
        if upper > nums[-1]: high = [nums[-1] + 1, upper]
        res = []
        if low: res.append(low)

        for i in range(len(nums) - 1):
            start, end = nums[i] + 1, nums[i + 1] - 1
            if start > end: continue
            if start <= lower <= end or start <= upper <= end or lower <= start <= upper or lower <= end <= upper:
                res.append([max(start, lower), min(upper, end)])

        if high: res.append(high)
        return res
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.findMissingRanges([0,1,3,50,75], 0, 99))
    print(sol.findMissingRanges([-1], -1, -1))

# Each pair of consecutive indices is an interval (start, end).
# If (lower, upper) and that interval overlap, the missing range is (max(start + 1, lower), min(end - 1, upper)) since we don't want to include start/end, just the overlap.