from collections import Counter

class Solution:
    def topKFrequent(self, nums, k: int):
        count = Counter(nums)
        frequencies = [(val, freq) for (freq, val) in count.items()]
        frequencies.sort(reverse=True)
        res = []
        for i in range(k):
            res.append(frequencies[i][1])
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1,1,1,2,2,3], 2))

# Quickselect for O(N)