class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = [int(digit) for digit in str(n)]
        i = len(digits) - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        if i == -1: return -1
        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1
        digits[i], digits[j] = digits[j], digits[i]
        
        left = i + 1
        right = len(digits) - 1
        while left < right:
            digits[left], digits[right] = digits[right], digits[left]
            left += 1
            right -= 1

        res = int(''.join(map(str,digits)))
        return res if res <= 2**31 - 1 else -1

# It's Next Permutation.