from collections import Counter

class Solution:
    def relativeSortArray(self, arr1, arr2):
        count1 = Counter(arr1)
        count2 = Counter(arr2)
        diff = []
        for elem in count1:
            if elem not in count2:
                dummy = [elem]*count1[elem]
                diff.extend(dummy)
        
        res = []
        for num in arr2:
            dummy = [num]*count1[num]
            res.extend(dummy)
        diff.sort()
        res.extend(diff)
        return res
    
if __name__ == "__main__":
    sol = Solution()
    # print(sol.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))
    # print(sol.relativeSortArray([28,6,22,8,44,17], [22,28,8,6]))
    print(sol.relativeSortArray([2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31], [2,42,38,0,43,21]))

# Have 2 hash tables to keep track of the frequencies of each element in both arrays
# Find elements in arr1 that don't exist in arr2, store them into a sorted array
# For each element in arr2, append the result array with the frequency of that respective element in arr1
# Merge the result array with the sorted array


        