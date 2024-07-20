from collections import defaultdict

class Solution:
    def twoSum(self, nums, target: int):
        hash_sum = defaultdict(int)
        
        for (i, num) in enumerate(nums):
            if num in hash_sum:
                return [hash_sum[num], i]
            
            hash_sum[target - num] = i
        


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))
    print(sol.twoSum([3, 2, 4], 6))
    print(sol.twoSum([3, 3], 6))

# Store the difference between the target and a number along with its index in a hash table
# When we reach that difference in a different number in the array, that's the pair we want

