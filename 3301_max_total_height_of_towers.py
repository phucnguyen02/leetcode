class Solution:
    def maximumTotalSum(self, maximumHeight) -> int:
        seen = set()
        maximumHeight.sort(reverse=True)
        max_height_so_far = maximumHeight[0]
        res = 0
        for height in maximumHeight:
            if height in seen:
                if max_height_so_far in seen or max_height_so_far <= 0:
                    return -1
                else:
                    seen.add(max_height_so_far)
                    res += max_height_so_far
            else:
                seen.add(height)
                res += height
            max_height_so_far = min(max_height_so_far - 1, height - 1)

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumTotalSum([2,3,4,3]))
    print(sol.maximumTotalSum([2, 2, 1]))

# Use sorting and greedy
# The intuition is that we want to pick the heights for the highest towers first since there's more options and we can just the shorter towers accordingly.
# Use a variable called max_height_so_far to keep track of highest possible number we can use for a tower so far, starting with maxHeights[0]
# Since we want each number to be unique, use a set to keep track of the heights so far.
# For each height we haven't seen yet, add it to the seen set and add it to the sum
# The max height so far then would be the minimum of itself - 1 and the current height - 1 since we want to account for cases where there might be multiple of the same
# heights in a row or we get a new height that's way lower than the previous
# If we've seen a tower height before, we use max_height_so_far and see if it's also seen or if it's reached 0. If either of those happens, we return -1. Otherwise, proceed like normal.