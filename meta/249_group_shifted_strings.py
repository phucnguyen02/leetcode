from collections import defaultdict
import itertools
class Solution:
    def groupStrings(self, strings):
        shifts = defaultdict(list)
        for string in strings:
            diff = [(ord(b) - ord(a)) % 26 for a,b in itertools.pairwise(string)]
            shifts[tuple(diff)].append(string)
        return shifts.values()

if __name__ == "__main__":
    sol = Solution()
    print(sol.groupStrings(["abc","bcd","acef","xyz","az","ba","a","z"]))
    
# For any 2 strings, if the pairwise differences between every consecutive characters in the string are exactly the same,
# then shifting them would eventually yield the same result. For example, "abc" has a difference of (1, 1), and "zab" also has a difference of (1, 1).
# This means they are part of the same group.
#  