class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # Initialize seen_once and seen_twice to 0
        seen_once = seen_twice = 0

        # Iterate through nums
        for num in nums:
            # Update using derived equations
            seen_once = (seen_once ^ num) & (~seen_twice)
            seen_twice = (seen_twice ^ num) & (~seen_once)

        # Return integer which appears exactly once
        return seen_once
    
# Keep track of 2 bitmasks: seen_once and seen_twice, to track the number of times a number has appeared.
# Every time we see a number, xor its bits with seen_once. If it's the first time we see that number then its bits
# will be 1 in seen_once. If it's the second time then they will be 0, and seen_twice would reflect that.
# If it's the third, both seen_once and seen_twice would be 0 for those bits. We and them with the inverse of the other mask
# so that the bits only appear once in either mask.