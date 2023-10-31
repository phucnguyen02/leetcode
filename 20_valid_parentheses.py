class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        if len(s) == 1: return False
        stack = []
        valid = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch not in valid:
                stack.append(ch)
            else:
                if stack and stack[-1] == valid[ch]:
                    stack.pop()
                else: return False
        return not stack


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid('{}[]()'))
    print(sol.isValid('[()]'))
    print(sol.isValid(')'))
    print(sol.isValid('(]'))
    print(sol.isValid(')(){}'))

#Use a stack to store only the opening brackets. If a closing bracket matches the front of the stack, then we pop.
#Otherwise, it's an invalid string.
#If the string is empty then we have popped all the correct pair of corresponding brackets.

#Initialize stack s
#For character in s:
#If character is an opening bracket then push it into s
#Else compare it to the front of the stack, if they match in terms of brackers then we pop s, otherwise we return false
#Returns true if s is empty, false otherwise