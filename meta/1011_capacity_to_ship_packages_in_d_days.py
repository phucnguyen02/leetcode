class Solution:
    def can_ship(self, weights, days, cap):
        total = 0
        weight_so_far = 0
        for weight in weights:
            if weight_so_far + weight > cap:
                total += 1
                weight_so_far = 0
            weight_so_far += weight
        return total + 1 <= days
    
    def shipWithinDays(self, weights, days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2
            if self.can_ship(weights, days, mid):
                right = mid

            else:
                left = mid + 1

        return left
    
# Binary search between max weights and sum of weights to get the first capacity number that allows shipment within D days