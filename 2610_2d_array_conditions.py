from collections import Counter

class Solution:
    def findMatrix(self, nums):
        count = Counter(nums)
        res = []
        for num in count:
            for i in range(count[num]):
                if i == len(res):
                    res.append([])
                res[i].append(num)
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.findMatrix([1,3,4,1,2,3,1]))
    print(sol.findMatrix([1,2,3,4]))

# Track the count of each element in the array. Then, corresponding to each element's count, append it to an array in the results array.
# Every time the count is equal to the length of the results array, we append an empty array into the results array so that the element can be added to that empty array.