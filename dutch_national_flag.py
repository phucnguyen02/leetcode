class Solution:
    def dutch_national_flag(self, arr, pivot):
        n = len(arr)
        if n < 2 or pivot < 0 or pivot >= n: return arr
        left = 0
        right = n-1
        for i in range(n):
            if arr[i] < arr[pivot]:
                arr[i], arr[left] = arr[left], arr[i]
                left += 1
        for i in range(n - 1, -1 ,-1):
            if arr[i] > arr[pivot]:
                arr[i], arr[right] = arr[right], arr[i]
                right -= 1
        return arr

if __name__ == "__main__":
    sol = Solution()
    print(sol.dutch_national_flag([1, 5, 4, 3, 9, 0], 3))
    print(sol.dutch_national_flag([1, 5, 4, 3, 9, 0], 10))
    print(sol.dutch_national_flag([1, 5, 4, 3, 9, 0], -1))
    print(sol.dutch_national_flag([1], 1))
    print(sol.dutch_national_flag([], 1))

#Have it so that we have 2 counters going from the start of the array for swapping numbers smaller than the pivot,
#and the end of the array backwards for swapping numbers smaller than the pivot.

#left = 0, right = n - 1
#For i = 0, ..., n - 1
#If arr[i] < arr[pivot] then swap arr[i] and arr[left] and increment left
#For i = n - 1, ..., 0
#If arr[i] > arr[pivot] then swap arr[i] and arr[right] and decrement right