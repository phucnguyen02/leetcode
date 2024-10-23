class Solution:
    def twoSum(self, numbers, target: int):
        L = 0
        R = len(numbers) - 1
        while L < R:
            sum = numbers[L] + numbers[R]
            if sum == target:
                return [L + 1, R + 1]

            elif sum < target:
                L += 1
            else:
                R -= 1