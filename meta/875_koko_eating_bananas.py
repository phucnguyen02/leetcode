import math

class Solution:
    def eat_all(self, piles, speed, h):
        hours = 0
        for banana in piles:
            hours += math.ceil(banana / speed)
        return hours <= h
    
    def minEatingSpeed(self, piles, h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            if self.eat_all(piles, mid, h):
                right = mid
            else:
                left = mid + 1

        return left
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minEatingSpeed([3,6,7,11], 8))
    print(sol.minEatingSpeed([30,11,23,4,20], 5))
    print(sol.minEatingSpeed([30,11,23,4,20], 6))

# Do binary search between 1 and the highest banana count to determine the smallest speed at which Koko can eat all the bananas
# Don't do it from min to max because it wouldn't work for a case where min = max