from collections import defaultdict

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set("aeiou")
        vowel_count = defaultdict(int)

        consonants = 0
        left = 0
        n = len(word)
        res = 0

        for right in range(n):
            if word[right] in vowels:
                vowel_count[word[right]] += 1
            else: consonants += 1

            while consonants > k:
                if word[left] in vowel_count:
                    vowel_count[word[left]] -= 1
                    if vowel_count[word[left]] == 0:
                        del vowel_count[word[left]]
                else:
                    consonants -= 1
                left += 1

            if len(vowel_count) == 5 and consonants == k:
                print(word[left:right+1])
                res += 1
                lf = left
                vs2 = vowel_count.copy()
                cc2 = consonants
                while len(vs2) == 5 and consonants == k:
                    if word[lf] in vs2 :
                        vs2[word[lf]]-=1
                        if vs2[word[lf]] == 0: 
                            del vs2[word[lf]]
                    else:
                        cc2-=1
                    lf+=1
                    if cc2==k and len(vs2)==5:
                        res+=1

        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.countOfSubstrings("aeioqq", 1))
    print(sol.countOfSubstrings("aeiou", 0))
    print(sol.countOfSubstrings("ieaouqqieaouqq", 1))