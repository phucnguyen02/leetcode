class Solution:
    def ship_all(self, capacity, weights, days):
        total_days = 1
        weight_so_far = 0
        for weight in weights:
            if weight_so_far + weight > capacity:
                total_days += 1
                weight_so_far = 0

            weight_so_far += weight
        

        return total_days <= days
    def shipWithinDays(self, weights, days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2

            if self.ship_all(mid, weights, days):
                right = mid

            else:
                left = mid + 1

        return left
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))
    print(sol.shipWithinDays([3,2,2,4,1,4], 3))