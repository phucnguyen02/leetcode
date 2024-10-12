class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for ch in s:
            if ch in "()":
                if stack and stack[-1] == "(" and ch == ")":
                    stack.pop()
                else:
                    stack.append(ch)

        return len(stack)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minAddToMakeValid("())"))
    print(sol.minAddToMakeValid("((("))
    print(sol.minAddToMakeValid("()))(("))

# Use a stack to store the brackets that don't have a corresponding partner