class Solution:
    def minFlips(self, target: str) -> int:
        after = "0"
        n = len(target)
        s = "0"*n
        if s == target: return 0

        res = 0
        for i in range(n):
            if after != target[i]:
                after = "1" if after == "0" else "0"
                res += 1

        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.minFlips("10111"))
    print(sol.minFlips("101"))

# Keep a variable that tracks what the suffix consists. At first the suffix is full of 0s.
# For every bit that's different from the target, flip the suffix. We can check this by comparing the suffix bit with the current bit.
# Return the total number of bits flipped