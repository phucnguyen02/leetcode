from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs):
        total = defaultdict(list)
        for str in strs:
            count = [0] * 26
            for ch in str:
                count[ord(ch) - ord('a')] += 1

            total[tuple(count)].append(str)

        return list(total.values())

if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))