from collections import Counter

class Solution:
    def getSneakyNumbers(self, nums):
        count = Counter(nums)
        return [i for i in count if count[i] > 1]