from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        leftmost = 0
        for i in range(len(s)):
            if s[i] < s[leftmost]: leftmost = i
            count[s[i]] -= 1
            if count[s[i]] == 0: break

        return s[leftmost] + self.removeDuplicateLetters(s[leftmost:].replace(s[leftmost], "")) if s else ""


if __name__ == "__main__":
    sol = Solution()
    #print(sol.removeDuplicateLetters("bcabc"))
    print(sol.removeDuplicateLetters("cbacdcbc"))

# The leftmost smallest letter in the string is always at the beginning of the solution.
# If there's a character larger than a character that comes after, and the first character has another occurrence later on,
# then delete the first character because the smaller character takes priority
# Use recursion to then check on the remainder of the string while replacing the smallest character with an empty one. 