class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = [digit for digit in str(num)]
        n = len(digits)

        max_digit_index = -1
        swap_index_1, swap_index_2 = -1, -1
        for i in range(n - 1, -1, -1):
            if max_digit_index == -1 or digits[i] >= digits[max_digit_index]:
                max_digit_index = i
            elif digits[i] < digits[max_digit_index]:
                swap_index_1 = i
                swap_index_2 = max_digit_index
        
        if swap_index_1 != -1 and swap_index_2 != -1:
            digits[swap_index_1], digits[swap_index_2] = digits[swap_index_2], digits[swap_index_1]
            return int("".join(digits))
                
        return num

if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumSwap(2736))


# The idea is that we want to move the largest digit that's the furthest to the right to the left in order to maximize our number.
# We also want to push it left as far as possible, provided the number it's replacing is less than it.
# Find the index of the highest digit for right to left. Make sure there's also a digit to the left that's less than it.
# The 2 digits that we want to swap are the furthest right digit that's the largest and the furthest left digit that's smaller than it.