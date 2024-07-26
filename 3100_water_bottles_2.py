class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = 0
        empty = 0
        while True:
            res += numBottles
            empty += numBottles
            if empty >= numExchange:
                numBottles = 1
                empty -= numExchange
                numExchange += 1
            else:
                return res
            
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxBottlesDrunk(13, 6))
    print(sol.maxBottlesDrunk(10, 3))

# Keep track of the number of empty bottles.
# If the number of empty bottles exceeds the exchangeable amount then exchange 1,
# drink it, and attempt to exchange the empty bottles again
# If you can't exchange anymore then you're done.
# The most efficient way to go about this is exchanging for 1 full bottle, drink it, and then exchange again