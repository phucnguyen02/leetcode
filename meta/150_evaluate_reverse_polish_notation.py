class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for ch in tokens:
            if ch in "+-/*":
                num1 = stack.pop()
                num2 = stack.pop()
                if ch == "+":
                    result = num1 + num2
                elif ch == "-":
                    result = num2 - num1
                elif ch == "*":
                    result = num1 * num2
                else:
                    result = int(num2 / num1)

                stack.append(result)
            else:
                stack.append(int(ch))

        return stack.pop()

if __name__ == "__main__":
    sol = Solution()
    print(sol.evalRPN(["2","1","+","3","*"]))
    print(sol.evalRPN(["4","13","5","/","+"]))

# Store the results in a stack. Every time we see an operation, pop the 2 elements at the top and do the appropriate operation, and push into stack.
