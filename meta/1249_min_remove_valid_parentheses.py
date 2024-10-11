class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove_indices = set()
        for (i, ch) in enumerate(s):
            if ch == "(":
                stack.append((ch, i))
            elif ch == ")":
                if not stack:
                    remove_indices.add(i)
                else:
                    stack.pop()
        while stack:
            remove_indices.add(stack.pop()[1])

        res = [s[i] for i in range(len(s)) if i not in remove_indices]
        return "".join(res)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minRemoveToMakeValid("lee(t(c)o)de)"))
    print(sol.minRemoveToMakeValid("a)b(c)d"))
    print(sol.minRemoveToMakeValid("))(("))
    
# Use a set to store which indices we don't want to include in our final string.
# Use a stack to store open brackets and their indices. Every time we encounter a closing bracket, it would be paired with the top of the stack,
# which is the closest opening bracket. We pop the opening bracket.
# If the stack is empty, that means there aren't anymore valid opening brackets before the current closing bracket, so we do not want to include it in the final string
# If the stack is still non-empty after iterating through the original string, that means there are some opening brackets that don't have their closing brackets. We
# don't want to include those in the final string either.
# Thus, with all of those indices in consideration, don't include them in the final string