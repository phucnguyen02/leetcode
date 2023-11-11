class Solution:
    def next_permutation(self, arr):
        if not arr: return []
        n = len(arr)
        target = n - 2
        while target >= 0 and arr[target] >= arr[target+1]:
            target -= 1
        if target == -1: return -1
        for i in range(n - 1, -1, -1):
            if arr[target] < arr[i]:
                arr[target], arr[i] = arr[i], arr[target]
                break
        arr[target+1:] = reversed(arr[target+1:])
        return arr

if __name__ == "__main__":
    sol = Solution()
    print(sol.next_permutation([2,1,1,3]))
    print(sol.next_permutation([3,1,1,2]))
    print(sol.next_permutation([3,2,1,1]))

#We try to find the longest decreasing suffix of the array first, the element before that suffix will be swapped
#with the lowest element that's higher than it in the suffix. After that, we reverse the suffix to get the
#lexicographically smallest new suffix. This is our next permutation.

# target = n - 2
# while target >= 0 and arr[target] >= arr[target+1]:
#   target -= 1
# for i = n - 1, n - 2, ..., 0:
#   if arr[target] < arr[i]:
#       swap arr[target] and arr[i]
#       break
# reverse arr[target+1:]
# return arr