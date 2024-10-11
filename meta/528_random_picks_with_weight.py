from bisect import bisect_right
from random import randrange

class Solution:

    def __init__(self, w):
        self.sum = 0
        self.pref_sum = []
        for num in w:
            self.sum += num
            self.pref_sum.append(self.sum)

    def pickIndex(self) -> int:
        if len(self.pref_sum) == 1: return 0
        rand = randrange(0, self.sum)
        return bisect_right(self.pref_sum, rand)        


if __name__ == "__main__":
    sol = Solution([3, 14, 1, 7])
    print(sol.pickIndex())
    

# Use prefix sum to help emulate the probabilities
# Use a random number generator to get a number, see where the number falls among the prefix sum array with binary search, and return the appropriate index
# The bigger the gap is between 2 numbers, the more likely it is that the random number will tip in favor of the larger number.