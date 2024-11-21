class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN_INT = -(2 ** 31)
        if dividend == MIN_INT and divisor == -1:
            return 2 ** 31 -1

        dd = abs(dividend)
        dv = abs(divisor)
        res = 0
        while dd >= dv:
            x = 0
            while dd - (dv << (1 + x)) >= 0:
                x += 1
            res += 1 << x
            dd -= dv << x

        if (dividend < 0 and divisor >= 0) or (dividend > 0 and divisor <= 0):
            res = -res
        return res
    
# Multiply divisor exponentially by 2. Once we can't, reduce dividend by that 2 ** (power) * divisor, add 1 << power to the result and keep going.
# Since we can't multiply, we use bit shifting instead with power. If there's exactly 1 negative, change the sign of the result
# If the dividend is the minimum int and the divisor is -1, then it'll overflow, so return 2 ** 31 - 1