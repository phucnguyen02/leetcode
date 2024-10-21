class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        n = len(s)
        dp = [False]*n

        for i in range(n):
            for word in wordDict:
                if i + 1 - len(word) < 0: continue

                if i == len(word) - 1 or dp[i - len(word)]:
                    if s[i - len(word) + 1:i+1] == word:
                        dp[i] = True
                        break

        return dp[-1]
    
    def wordBreak_trie(self, s: str, wordDict) -> bool:
        n = len(s)
        dp = [False]*n
        root = TrieNode()
        for word in wordDict:
            cur = root
            for i in range(len(word)):
                ch = word[i]
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()

                cur = cur.children[ch]
            cur.is_end = True
            
        for i in range(n):
            if i == 0 or dp[i - 1]:
                cur = root
                for j in range(i, n):
                    ch = s[j]

                    if ch not in cur.children:
                        break

                    cur = cur.children[ch]

                    if cur.is_end:
                        dp[j] = True
        
        print(dp)
        return dp[-1]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.wordBreak_trie("leetcode", ["leet","code"]))

# DP without trie:
# DP(i) = whether you can segment s[:i + 1] into words in the dictionary.
# If we reach i, we check every word in the dictionary and subtract its length from i. If we were able to segment without that word included, then DP(i) = true.
# DP(i) = DP(i - word_len) for word in wordDict if s[i - word_len + 1:i + 1] == word

# With trie:
# If we reach i, we traverse the trie staring from s[i]. If we're able to reach the end of the trie, that means the substring from s[i] to some s[j] can be segmented.
# Thus, DP(j) = true. We only traverse the trie if DP(i - 1) = true because then, s[i] could be the start of the next valid segment.
