class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        res = [0]*len(temperatures)
        for (i, temp) in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                res[index] = i - index

            stack.append(i)
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))

# Mono decreasing stack to keep track of temps. Whenever a temp is popped, check its index, and increase the index-th element of the result by i - index