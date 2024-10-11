class Solution:
    def concatenate(self, first, second, third):
        return first * (2 ** (second.bit_length() + third.bit_length())) + second * (2 ** third.bit_length()) + third

    def maxGoodNumber(self, nums) -> int:
        return max(self.concatenate(nums[0], nums[1], nums[2]), self.concatenate(nums[0], nums[2], nums[1]),
        self.concatenate(nums[1], nums[0], nums[2]), self.concatenate(nums[1], nums[2], nums[0]),
        self.concatenate(nums[2], nums[1], nums[0]), self.concatenate(nums[2], nums[0], nums[1]))
    
# The binary concatenation of 3 numbers a, b, c in that order is the sum of c, b times 2 to the bit length of c, and a times 2 to the sum bit lengths of b and c.
# The reason for this is that a and b are placed earlier in the bit array, so we have to multiply by the powers of the bit length.