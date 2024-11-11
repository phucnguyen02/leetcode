from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False

class Solution:
    def addBoldTag(self, s: str, words) -> str:
        root = TrieNode()
        
        for word in words:
            cur = root
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                
                cur = cur.children[ch]
            
            cur.is_end = True

        is_bold = [False]*len(s)

        for i in range(len(s)):
            
            end = i
            cur = root
            for j in range(i, len(s)):
                ch = s[j]
                if ch not in cur.children:
                    break

                cur = cur.children[ch]
                if cur.is_end:
                    end = j + 1

            for j in range(i, end):
                is_bold[j] = True

        res = []

        for i in range(len(s)):
            if is_bold[i] and (i == 0 or not is_bold[i - 1]):
                res.append('<b>')

            res.append(s[i])

            if is_bold[i] and (i == len(s) - 1 or not is_bold[i + 1]):
                res.append('</b>')

        return "".join(res)
if __name__ == "__main__":
    sol = Solution()
    print(sol.addBoldTag("abcxyz123", ["abc","123"]))

# Have an array indicating which indices to bold
# Store all the dictionary words in a trie
# Iterate through each index of the word and attempt to find if a substring after it is in the trie. If so, mark every index in that window as true in the bold array