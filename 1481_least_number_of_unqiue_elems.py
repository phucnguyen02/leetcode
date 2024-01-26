from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr, k: int) -> int:
        freq = sorted([val for val in Counter(arr).values()])
        for i in range(len(freq)):
            subtract = min(k, freq[i])
            freq[i] -= subtract
            k -= subtract
            if k == 0: break
        
        return len([val for val in freq if val])

if __name__ == "__main__":
    sol = Solution()
    print(sol.findLeastNumOfUniqueInts([5, 5, 4], 1))
    print(sol.findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3))

# Hash table for all the frequencies of elems
# Remove the least frequent ones
# Return the total number of elements with frequency > 0
