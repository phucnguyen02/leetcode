class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        left = res = zeroes = ones = 0
        for (num, right) in enumerate(s):
            if num == "0": zeroes += 1
            else: ones += 1
            while left < right and zeroes > k and ones > k:
                if s[left] == "0": zeroes -= 1
                else: ones -= 1
                left += 1
            res += right - left + 1
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.countKConstraintSubstrings("10101", 1))
    print(sol.countKConstraintSubstrings("101010101", 2))
    
# Use a sliding window. Every time the window fits the constraint, add its count of substrings to the result.