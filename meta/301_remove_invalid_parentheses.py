from collections import defaultdict
from bisect import bisect_left, bisect_right

class Solution:
    def removeInvalidParentheses(self, s: str):
        count = defaultdict(set)
        print(bisect_left([2,5], 3), bisect_right([2, 5], 3))
        min_removed = len(s)
        def backtracking(index, stack, word, removed):
            nonlocal min_removed
            if index == len(s):
                if not stack:
                    min_removed = min(removed, min_removed)
                    count[removed].add(word)
                return
            if s[index] not in "()":
                backtracking(index + 1, stack, word + s[index], removed)
                return
            if stack and stack[-1] == "(" and s[index] == ")":
                backtracking(index + 1, stack[:-1], word + s[index], removed)
            else:
                backtracking(index + 1, stack + [s[index]], word + s[index], removed)

            backtracking(index + 1, stack, word, removed + 1)

        backtracking(0, [], "", 0)
        return list(count[min_removed])

if __name__ == "__main__":
    sol = Solution()
    print(sol.removeInvalidParentheses("()())()"))
            
# Do backtracking. At each step, we either include the current parentheses or don't include it.
# If we do include it, make sure the stack is updated correctly. If the top is ( and the cur character is ), then don't include the top of the stack. Otherwise, push it and continue to the next index
# If we don't include it, don't update the stack, but increase the number of removed parentheses so far.

# Once we reach the length of s, then check if the stack is empty. If it is, then we have a valid string now. Add the string along with its removed count to a hash table and update the min removed count
# At the end, check all of the strings in the min removed key of the hash table





