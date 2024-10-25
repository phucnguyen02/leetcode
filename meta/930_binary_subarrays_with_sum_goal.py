from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref_sum = 0
        hash_sum = defaultdict(int)
        hash_sum[0] = 1
        res = 0
        for (i, num) in enumerate(nums):
            pref_sum += num
            if pref_sum - goal in hash_sum:
                res += hash_sum[pref_sum - goal]
            hash_sum[pref_sum] += 1
        return res
    
# Use a hash table to store prefix sums. If prefix sum - k is already in the hash table then for the indices i it was incremented it, the subarrays from i + 1
# to the current index have subarray sum = k