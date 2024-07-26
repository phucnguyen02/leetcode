class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        empty = 0
        while True:
            res += numBottles
            empty += numBottles
            if empty >= numExchange:
                numBottles = empty // numExchange
                empty = empty % numExchange
            else:
                return res
            
if __name__ == "__main__":
    sol = Solution()
    print(sol.numWaterBottles(9, 3))
    print(sol.numWaterBottles(15, 4))

# Keep track of the number of empty bottles.
# If the number of empty bottles exceeds the exchangeable amount then exchange as many as possible,
# drink them all, and attempt to exchange the empty bottles again
# If you can't exchange anymore then you're done.