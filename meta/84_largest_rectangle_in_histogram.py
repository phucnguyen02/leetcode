class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for (i, h) in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                res = max(res, height * (i - index))
                start = index
            
            stack.append((start, h))
        
        for (i, h) in stack:
            res = max(res, h * (len(heights) - i))
        return res
    
# Use a mono increasing stack. For each height, store its start index, aka where it can expand to to the left (the first height larger than it).
# When we pop a height, its max range is its height * width (width = the current index - start)
# Do the same w/ the remaining elements in the monostack