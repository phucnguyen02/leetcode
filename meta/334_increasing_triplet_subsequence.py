class Solution:
    def increasingTriplet(self, nums) -> bool:
        if len(nums) < 3: return False
        num1 = num2 = float('inf')
        for num in nums:
            if num <= num1: num1 = num
            elif num <= num2: num2 = num
            else: return True
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.increasingTriplet([1, 2, 3, 4, 5]))
    print(sol.increasingTriplet([2, 3, 1]))
    print(sol.increasingTriplet([5, 4, 3, 2]))

# Have 2 numbers to keep track of the lowest and second lowest numbers so far. If there is a number larger than both then we have an increasing triplet. 
