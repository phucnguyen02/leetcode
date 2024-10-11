class Solution:
    def subarraySum(self, nums, k: int) -> int:
        sum = 0
        res = 0
        hash_sum = {0: 1}
        for num in nums:
            sum += num
            if sum not in hash_sum:
                hash_sum[sum] = 0
            
            if sum - k in hash_sum:
                res += hash_sum[sum - k]
            hash_sum[sum] += 1
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraySum([1,1,1], 2))
    print(sol.subarraySum([1, 2, 3], 3))