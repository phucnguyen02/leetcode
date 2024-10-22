class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        stack = [-1]
        res = 0
        for (i, ch) in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res
    
    def longestValidParentheses_o1(self, s: str) -> int:
        left = right = 0
        res = 0
        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            
            if right > left:
                right = left = 0
            elif right == left:
                res = max(res, left * 2)

        left = right = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            
            if right < left:
                right = left = 0
            elif right == left:
                res = max(res, left * 2)

        return res
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestValidParentheses("(()"))
    print(sol.longestValidParentheses(")()())"))

# Approach 1: Stack
# Each time we encounter (, append its index into the stack. When we see ), pop the stack.
# The length of a valid parentheses substring is the current index - the top of the stack.
# The reason why we get the top after we pop the stack is the top at that point is supposed to represent the index before the start of the valid substring.
# That's why at first, we put -1 into the stack because the substring could start from index 0. If ) is encountered before a (, then we discard the substring before that.
# Thus, every time we encounter a ), after we pop the stack and the stack is empty, then we append the current index as well

# Approach 2: Two Pointers
# Have left = right = 0, with left representing the ( count and right representing the ) count.
# Iterate forward. Increment left and right accordingly. If at any point, right > left then reset both. We want to start counting from the index after. If right == left then maximize the result and left * 2
# Iterate backward and do the same thing but with right < left as the reset condition instead.