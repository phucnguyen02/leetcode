from collections import defaultdict

class Solution:
    def canArrange(self, arr, k: int) -> bool:
        mod_freq = defaultdict(int)
        for num in arr:
            mod_freq[num % k] += 1
        for i in range(1, k):
            if mod_freq[i] != mod_freq[k - i]: return False
        if 0 in mod_freq: return mod_freq[0] % 2 == 0
        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.canArrange([1,2,3,4,5,10,6,7,8,9], 5))
    print(sol.canArrange([1,2,3,4,5,6], 7))
    print(sol.canArrange([1,2,3,4,5,6], 10))

# Store all the modulos by k for each number in a hash table. If freq[i] != freq[k - i] then return false because all of those numbers are supposed to be paired with each other.
# If 0 is a modulo then we can't compare with freq[k], so we have to see if it's even or not.
