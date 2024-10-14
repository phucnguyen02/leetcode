from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        required = len(t_count)
        s_count = defaultdict(int)
        res = [float('inf'), 0, 0]
        left = 0
        match = 0
        for i in range(len(s)):
            s_count[s[i]] += 1
            if s[i] in t_count and s_count[s[i]] == t_count[s[i]]: match += 1

            while match == required:
                if res[0] > i - left + 1:
                    res = [i - left + 1, left, i]
                
                s_count[s[left]] -= 1
                
                if s[left] in t_count and s_count[s[left]] < t_count[s[left]]: match -= 1
                left += 1

        return s[res[1]:res[2]+1] if res[0] != float('inf') else ""

if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))

# Use a hash set for both s and t, and the sliding window approach
# Keep track of when the number of characters within s_count matches the number of characters within t_count. When that happens, shrink the window
# while updating the number of matches accordingly. We also update the result indices that contain the shortest substring that satisfies the condition.