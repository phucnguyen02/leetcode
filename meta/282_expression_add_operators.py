class Solution:
    def addOperators(self, num: str, target: int):
        n = len(num)
        res = []
        def backtracking(index, prev_operand, cur_operand, value, string):
            if index == n:
                if value == target and cur_operand == 0:
                    res.append("".join(string[1:]))
                return
            
            cur_operand = cur_operand * 10 + int(num[index])
            
            if cur_operand > 0:
                backtracking(index + 1, prev_operand, cur_operand, value, string)
            
            string.append("+")
            string.append(str(cur_operand))
            backtracking(index + 1, cur_operand, 0, value + cur_operand, string)
            string.pop()
            string.pop()

            if string:
                string.append("-")
                string.append(str(cur_operand))
                backtracking(index + 1, -cur_operand, 0, value - cur_operand, string)
                string.pop()
                string.pop()

                string.append("*")
                string.append(str(cur_operand))
                backtracking(index + 1, cur_operand * prev_operand, 0, value - prev_operand + (cur_operand * prev_operand), string)
                string.pop()
                string.pop()

        def backtracking_pm_only(index, cur_operand, value, string):
            if index == n:
                if value == target and cur_operand == 0:
                    res.append("".join(string[1:]))
                return
            
            cur_operand = cur_operand * 10 + int(num[index])
            
            if cur_operand > 0:
                backtracking_pm_only(index + 1, cur_operand, value, string)
            
            string.append("+")
            string.append(str(cur_operand))
            backtracking_pm_only(index + 1, 0, value + cur_operand, string)
            string.pop()
            string.pop()

            if string:
                string.append("-")
                string.append(str(cur_operand))
                backtracking_pm_only(index + 1, 0, value - cur_operand, string)
                string.pop()
                string.pop()


        backtracking_pm_only(0, 0, 0, [])
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.addOperators("123", 6))

# There's 4 decisions at each index: use +, -, * or no operation and keep expanding the current number by adding the digit to the right of it
# We keep track of the current operand/number and adjust our current value along the way so as to compare it to the target in O(1) when we're at the end.
# When we're at the end, it has to be after we did an operation with the last digit, instead of trying to expand it even more.
# The * complicates things. If we have a *, then we have to keep track of the previous operand as well, so that we may reverse the effect and multiply it with the current operand