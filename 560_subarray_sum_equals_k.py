from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k: int) -> int:
        res = sum = 0
        sum_freq = defaultdict(int)
        sum_freq[0] = 1
        for num in nums:
            sum += num
            if sum - k in sum_freq:
                
                res += sum_freq[sum - k]
            sum_freq[sum] += 1
        return res
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraySum([1, 2, 3, -1, 1, 0, 4, -5], 4))


# Use prefix sum and store that prefix sum in a hash table. We use the difference between the prefix sum and k in order
# to determine the subarray with sum equals k. The count of a prefix sum represents how many times a subarray with that
# sum has appeared.