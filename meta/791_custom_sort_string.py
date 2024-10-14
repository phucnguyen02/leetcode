from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_count = Counter(s)
        res = ""
        for ch in order:
            if ch in s_count:
                res += ch * s_count[ch]
                s_count[ch] = 0
        for ch in s:
            if s_count[ch]:
                s_count[ch] -= 1
                res += ch
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.customSortString("cba", "abcd"))
    print(sol.customSortString("bcafg", "abcd"))
    print(sol.customSortString("kqep", "pekeq"))


# Iterate through each character in order and see if it exists in s
# If it does, append every single instance of that character into the final string and set the frequency to 0.
# Once we're done with the order, just append any remaining characters in s that haven't been added yet