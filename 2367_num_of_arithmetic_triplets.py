from collections import defaultdict

class Solution:
    def arithmeticTriplets(self, nums, diff: int) -> int:
        hash_table = defaultdict(int)
        for num in nums:
            hash_table[num] = hash_table[num - diff] + 1

        return len([key for key in hash_table if hash_table[key] >= 3])
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.arithmeticTriplets([0,1,4,6,7,10], 3))
    print(sol.arithmeticTriplets([4, 5, 6, 7, 8, 9], 2))

# Use a hash table to see which elements at the end of a triplet correspond to an arithmetic triplet.
# We subtract the current element by the difference and store it as the entry for that element in the hash table + 1, corresponding to the
# length of an increasing array whose elements differ by exactly diff.
# If the length is above 3 then we add it to the result