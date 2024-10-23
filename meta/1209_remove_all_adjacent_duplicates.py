class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if not stack or char != stack[-1][0]:
                stack.append([char, 1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
        return "".join(c * count for c, count in stack)
            
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates("abcd", 2))
    print(sol.removeDuplicates("deeedbbcccbdaa", 3))

# Store the characters and their counts so far in the stack.
# If the stack is empty or the current character is different from the top then add it to the stack
# Otherwise, increment the count. If the count reaches k then pop the stack
# At the end, the string is all of the characters in the stack times their counts
