class Solution:
    def countPairs(self, nums) -> int:
        res = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1 , len(nums)):

                n1 = str(nums[i])
                n2 = str(nums[j])

                if len(n1) < len(n2):
                    n1 = '0' * abs(len(n1) - len(n2)) + n1

                elif len(n1) > len(n2):
                    n2 = '0' * abs(len(n1) - len(n2)) + n2

                diff = 0

                for i in range(len(n2)):
                    if n1[i] != n2[i]:
                        diff += 1

                if diff <= 2 and sorted(n1) == sorted(n2):
                    res += 1
        return res
	
if __name__ == "__main__":
    sol = Solution()
    print(sol.countPairs([3,12,30,17,21]))
    print(sol.countPairs([1, 1, 1, 1, 1]))
    print(sol.countPairs([123, 321]))


# Check every pair in the array since the constraints allow it
# Add any trailing 0s to the number with the smaller length
# Compare the new numbers with each other. If there are less than 2 differences then those different digits could be swapped to create the other number.
# However, there could also be the case that 2 numbers have every equal digit in the same position except for 1, so we have to sort the arrays of the numbers
# too to check.