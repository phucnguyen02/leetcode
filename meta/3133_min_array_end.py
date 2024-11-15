class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        i_x = i_n = 1

        while i_n <= n - 1:
            if i_x & x == 0:
                if i_n & (n - 1):
                    res |= i_x
                i_n *= 2
            i_x *= 2
        
        return res
    
# What we care about is the set bits of x, because those have to remain unchanged. The reason is that if we do AND on every number,
# all of them have to have the same set bits as x in order to get x
# The smallest element has to be x because otherwise, we'd lose those set bits.
# Since we're getting n - 1 extra elements with set bits like x's, we iterate through x and fill in the bits of n - 1 only for bits that weren't set in x