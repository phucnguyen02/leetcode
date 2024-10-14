class Solution:
    def exclusiveTime(self, n: int, logs):
        res = [0]*n
        stack = []
        for log in logs:
            id, flag, time = log.split(":")
            time = int(time)
            if flag == "start":
                if stack:
                    stack[-1][2] += time - stack[-1][1] 
                stack.append([int(id), time, 0])
            elif flag == "end":
                id, last_start, runtime = stack.pop()
                runtime += time - last_start + 1
                res[id] += runtime
                if stack:
                    stack[-1][1] = time + 1
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]))
    print(sol.exclusiveTime(1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]))
    print(sol.exclusiveTime(2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]))


# Since 2 functions can't be ran at once, we use a stack to update which function is running (aka the top of the stack).
# For each element/function in the stack, we store the id, the last time it started running, and its total runtime so far. We ignore the fact that
# multiple functions can have the same id

        