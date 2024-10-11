class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = arr.count(0)
        n = len(arr)
        for i in range(n - 1, -1, -1):
            if i + zeros < n:
                arr[i + zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < n:
                    arr[i + zeros] = 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.duplicateZeros([1,0,2,3,0,4,5,0]))
# First keep track of the number of 0s in the array.
# Iterate through the array backwards. The number of 0s behind a number is how many positions it's gonna get pushed forward.
# If there's a 0 then we subtract the count and repeat the same process to emulate the duplication