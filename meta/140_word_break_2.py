class Solution:
    def wordBreak(self, s, wordDict):
        res = []
        def backtracking(start, sentence):
            if start == len(s):
                res.append(" ".join(sentence))
                return
            
            for i in range(start, len(s)):
                substring = s[start:i + 1]
                if substring in wordDict:
                    sentence.append(substring)

                    backtracking(i + 1, sentence)
                    sentence.pop()

        backtracking(0, [])
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.wordBreak("catsanddog", ["cat","cats","and","sand","dog"]))
    print(sol.wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]))
        
# Do backtracking. For every start index, attempt to expand the end index and see if the formed word is within the dictionary.
# If so, add the word into the sentence and move the start index to be after the end index
# If start == len(s) then we reached the end of s and all of the previously added words are part of the dictionary, so we add the sentence into result