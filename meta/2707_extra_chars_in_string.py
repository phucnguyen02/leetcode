class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def minExtraChar(self, s: str, dictionary) -> int:
        root = TrieNode()
        for word in dictionary:
            cur = root
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                
                cur = cur.children[ch]
            
            cur.is_end = True
        
        dp = [0] * (len(s) + 1)
        
        for start in range(len(s) - 1, -1, -1):
            dp[start] = dp[start + 1] + 1
            node = root
            for end in range(start, len(s)):
                if s[end] not in node.children:
                    break
                node = node.children[s[end]]
                if node.is_end:
                    dp[start] = min(dp[start], dp[end + 1])
        return dp[0]
    
# Use Trie to store dictionary words
# DP(i) backwards to store the minimum characters to be added starting from i.
# DP(i) = min(DP(i), DP(end + 1)) if s[i:end + 1] forms a word