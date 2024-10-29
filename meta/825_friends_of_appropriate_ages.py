from bisect import bisect_right
from collections import Counter
class Solution:
    def numFriendRequests(self, ages) -> int:
        ages.sort()
        res = 0
        for age in ages:
            right = bisect_right(ages, age)
            left = bisect_right(ages, 0.5 * age + 7) + 1
            res += max(0, right - left)

        return res
    
    def numFriendRequests(self, ages):
        count = Counter(ages)
        ans = 0
        for ageA, countA in count.items(): 
            for ageB, countB in count.items():
                if ageA * 0.5 + 7 >= ageB: continue
                if ageA < ageB: continue
                ans += countA * countB
                if ageA == ageB: ans -= countA

        return ans
    
# For each age, do a binary search to find the highest index i where every element from 0 to i - 1 <= age, and the highest index i
# where every element from 0 to i - 1 < 0.5 * age + 7. That is the range of the friends we can send requests to. If left > right then add 0

# O(N):
# Keep track of the frequencies for every age.
# Do a nested for loop through every pair of ages.
# If ageA can add ageB then we increment the result by the count of ageA * the count of ageB. If ageA = ageB then we subtract it by the count of ageA because
# people can't add themselves as friends.
