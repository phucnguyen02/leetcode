class Solution:
    def gcdOfStrings(self, str1, str2) -> str:
        if str1 == str2: return str1
        if len(str1) > len(str2): return self.gcdOfStrings(str2, str1)
        l1 = len(str1)
        l2 = len(str2)
        res = ""
        for pref_length in range(1, l1 + 1):
            prefix = str1[:pref_length]
            if l1 % pref_length == 0 and l2 % pref_length == 0:
                if prefix*(l1 // pref_length) == str1 and prefix*(l2 // pref_length) == str2:
                    res = prefix

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.gcdOfStrings("ABCABC", "ABC"))
    print(sol.gcdOfStrings("ABABAB", "AB"))
    print(sol.gcdOfStrings("LEET", "CODE"))

# The result has to be a prefix if the concatenation of multiple of it creates both of the strings
# Check all of the prefixes for the smaller string and see if multiple of them can create the two strings