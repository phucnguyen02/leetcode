class Solution:
    def findBuildings(self, heights):
        stack = []
        bad_indices = set()
        for (i, height) in enumerate(heights):
            while stack and stack[-1][1] <= height:
                index, hght = stack.pop()
                bad_indices.add(index)
            stack.append((i, height))

        res = [i for i in range(len(heights)) if i not in bad_indices]
        return res
    
    def findBuildings(self, heights: List[int]) -> List[int]:
        cur_max = -1
        res = []
        for i in range(len(heights) - 1, -1, -1):
            if cur_max < heights[i]:
                cur_max = heights[i]
                res.append(i)

        return res[::-1]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.findBuildings([4,2,3,1]))
    print(sol.findBuildings([4, 3, 2, 1]))
    print(sol.findBuildings([1, 3, 2, 4]))

# We use a monotonically decreasing stack to keep track of valid buildings.
# Buildings that never get popped out of the stack are ones whose right neighbors aren't taller than them
