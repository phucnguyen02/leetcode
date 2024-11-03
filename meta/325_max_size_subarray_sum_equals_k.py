class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        hash_sum = {0: -1}
        res = 0
        pref_sum = 0
        for (i, num) in enumerate(nums):
            pref_sum += num
            if pref_sum - k in hash_sum:
                res = max(res, i - hash_sum[pref_sum - k])
            
            if pref_sum not in hash_sum:
                hash_sum[pref_sum] = i

        return res
    
# Use prefix sum since it's a problem related to subarray sum
# Notice that if sum - k is in the stored hash table of sums then its first appearance is the left index, and i is the right index, and they create a subarray sum of k