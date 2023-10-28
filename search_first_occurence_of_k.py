class Solution:
    def first_occurence(self, arr, k):
        l = 0
        r = len(arr)-1
        while l < r:
            m = (l + r) // 2
            if arr[m] >= k:
                r = m
            else:
                l = m + 1
        return l


if __name__ == "__main__":
    sol = Solution()
    print(sol.first_occurence([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 243))

#L = 0, R = len(arr) - 1
#while L < R:
#Do binary search to find largest i such that arr[i] < k
#Return i + 1

#Find largest index i such that arr[i] < k. Answer will be i+1.