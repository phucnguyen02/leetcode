from collections import defaultdict

class Solution:
    def minSubarray(self, nums, p: int) -> int:
        total = sum(nums)
        if total % p == 0: return 0

        target = total % p
        pref_sum = 0
        n = len(nums) 
        removed = n
        modulo_table = defaultdict(int)
        modulo_table[0] = -1
        for (i, num) in enumerate(nums):
            pref_sum = (pref_sum + num) % p
            needed = (pref_sum - target) % p
            if needed in modulo_table:
                removed = min(i - modulo_table[needed], removed)

            modulo_table[pref_sum] = i

        return removed if removed != n else -1 
    
# First, calculate the sum of the array, and take its remainder when divided by p, call it target.
# In order for the sum to be divisible by p, we have to remove the smallest subarray whose sum % p = target
# So let's say the subarray up to index i and index j with j > i has the subarray between from i + 1 to j, and its sum % p = target.
# So its sum is (sum[j] - sum[i]) % p == target. So if we want to find that (i + 1, j) subarray, we remove the prefix subarray until i.
# To find it, its prefix sum is (sum[j] - target + p) % p. Thus, we also use a hash table to store the prefix sums and their last appearances.


