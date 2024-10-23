class Solution:
    def generateParenthesis(self, n: int):
        res = []
        def backtracking(index, stack, word):
            if index == n * 2:
                if not stack:
                    res.append("".join(word))
                return

            if len(stack) > n:
                return
            
            for ch in "()":
                word.append(ch)
                if ch == "(":
                    stack.append(ch)
                    backtracking(index + 1, stack, word)
                    stack.pop()
                else:
                    if stack:
                        stack.pop()
                        backtracking(index + 1, stack, word)
                        stack.append("(")
                word.pop()
        backtracking(0, [], [])
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(3))
            
# Do backtracking on every possible combination of (). Stop when the index == n * 2 since that'd be the length of the string
# Use a stack to store the current state of valid parentheses. If ( is in then ) pops it. If the stack is empty we have a valid parentheses string
# Optimizations:
# If the stack is empty then there's no point in pushing ) in if it's never gonna get popped, thus never getting us a valid string
# If the length of the stack is more than n then we have pushed ( in more than n times, and we can't pop it in more than n times since the iterations would be more than n * 2.