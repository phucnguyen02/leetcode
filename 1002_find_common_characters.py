from collections import Counter

class Solution:
    def commonChars(self, words):
        count = Counter(words[0])
        for word in words[1:]:
            count &= Counter(word)

        res = []
        for ch in count:
            for _ in range(count[ch]):
                res.append(ch)
        return res

        
if __name__ == "__main__":
    sol = Solution()
    print(sol.commonChars(["bella","label","roller"]))
        

# Use list intersection + hash map counting the frequency of each letter to find the common letters